# Import all the models, so that Base has them before being
# imported by Alembic
from centaur.db.base_class import Base  # noqa
