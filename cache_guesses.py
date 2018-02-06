import pickle
from tqdm import tqdm
from nltk.corpus import stopwords as sw
from bs4 import BeautifulSoup

from qanta.preprocess import tokenize_question
from guesser_buzzer_client import GuesserBuzzer
from util import highlight_prefix, highlight_suffix
from util import QBQuestion, QantaCacheEntry

stopwords = set(sw.words('english'))

def get_matched(q: QBQuestion, position, matches):
    '''
    For a (partial) question and a list of matched documents (with highlights)
    Args:
        q: the QBQuestion.
        position (int): so the partial question is `q.raw_text[:position]`
        matches: list of matches
    '''
    # take the top 2 mathces from both qb and wiki
    matches = matches['qb'][:2] + matches['wiki'][:2]

    # find words highligted in the matches
    highlighted_words = set() # words highlighted in the matches
    for match in matches:
        soup = BeautifulSoup(match)
        match = [x.text.lower() for x in soup.find_all('em') 
                if x.text.lower() not in stopwords and len(x.text) > 2]
        highlighted_words.update(match)

    # find the highlighted words in the question
    matched_words = set() # words matched in the question
    text_highlight = [] # mark highlight or not in the displayed text
    for ts in q.tokens[:position]:
        matched = [t in highlighted_words for t in ts]
        text_highlight.append(any(matched))
        matched_words.update(t for t, m in zip(ts, matched) if m)

    # mark words in the matches
    tokenized_matches = []
    matches_highlight = []
    for m in matches:
        tokenized_matches.append([])
        matches_highlight.append([])
        m = m.replace('<em>', '__').replace('</em>', ' ') 
        for word in m.split():
            if not word.startswith('__'):
                tokenized_matches[-1].append(word)
                matches_highlight[-1].append(False)
            else:
                word = word[2:] # remove __ prefix
                ts = tokenize_question(word)
                matched = [t in matched_words for t in ts]
                matches_highlight[-1].append(any(matched))
                tokenized_matches[-1].append(word)
    return text_highlight, tokenized_matches, matches_highlight
        
def get_cache(gb, q):
    gb.new_question(q.qid)
    entries = dict() # position -> QantaCacheEntry
    entry = None
    for i in range(1, q.length + 1): # +1 because we take [:i]
        if i % 5 == 1:
            sentence = ' '.join(q.raw_text[:i])
            buzz_scores = gb.buzz(sentence, i)
            text_highlight, tokenized_matches, matches_highlight = \
                get_matched(q, i, gb.matches)
            # text_highlight, tokenized_matches, matches_highlight = None, None, None
            entry = QantaCacheEntry(q.qid, i, gb.answer, gb.guesses,
                    buzz_scores, tokenized_matches, text_highlight,
                    matches_highlight)
        assert entry is not None
        entries[i] = entry
    return entries

def main():
    gb = GuesserBuzzer()
    with open('data/questions.pkl', 'rb') as f:
        questions = pickle.load(f)

    # questions = questions[:10]

    records = dict()
    for q in tqdm(questions):
        records[q.qid] = get_cache(gb, q)

    with open('data/cache.pkl', 'wb') as f:
        pickle.dump(records, f)

if __name__ == '__main__':
    main()
