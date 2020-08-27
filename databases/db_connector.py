from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from logger import logging
from databases import db_connector_retrying

from settings import DATABASE_URL


class DbConnector:

    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        Session = sessionmaker(self.engine)
        self.session = Session()

    def exec_query_without_retry(self, obj, params):
        return self.session.execute(obj, params)

    def exec_query(self, obj, **params):
        return db_connector_retrying.run_query(self.session, self.exec_query_without_retry, 2, obj, params)

    def update(self, model, id, data):
        db_connector_retrying.run_query(self.session, self.update_without_retry, 2, model, id, data)

    def update_without_retry(self, model, id, data):
        self.session.query(model).filter(model.id == id).update(data)
        self.session.commit()

    def close(self):
        self.session.commit()
        self.session.close()
        self.engine.dispose()
