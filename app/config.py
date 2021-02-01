from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import logging

DATABASE_URL = 'postgresql+psycopg2://liz:password@localhost/bucketlist'
DB_ECHO = False
DB_AUTOCOMMIT = True


def get_engine(uri):
    logging.info('Connecting to database...')
    options = {
        'echo': DB_ECHO,
        'execution_options': 
            {'autocommit': DB_AUTOCOMMIT}
    }

    return create_engine(uri, **options)


def init_session():
    db_session.configure(bind=engine)
    from app.models import Base
    Base.metadata.create_all(engine)

db_session = scoped_session(sessionmaker())
engine = get_engine(DATABASE_URL)

