import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="augment",
    version="0.0.1",
    author="HyoJung",
    author_email="hjhan@cs.umd.edu",
    description="Code for http://simqa.cs.umd.edu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h-j-han/xqb_interface",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'pandas',
        'sqlalchemy',
        'psycopg2-binary',
        'autobahn',
        'twisted',
        
    ]
)
