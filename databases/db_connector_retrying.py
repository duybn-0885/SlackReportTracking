import sqlalchemy as SA
from logger import logging


def warning(session, e):
    logging.warning("Database connection has problem. Retrying...: %s" % e)
    session.rollback()

def catch_exception(session, e):
    logging.error("DbConnectorRetrying error. Catch exception with traceback")
    logging.exception(e)
    session.rollback()

def run_query(session, f, attempts=3, *args):
    while attempts >= 0:
        attempts -= 1
        try:
            return f(*args)
        except SA.exc.DBAPIError as exc:
            if attempts >= 0:
                warning(session, exc)
            else:
                catch_exception(session, exc)
                raise
        except Exception:
            session.rollback()

def run_query_without_raise(session, f, attempts=3, *args):
    while attempts >= 0:
        attempts -= 1
        try:
            return f(*args)
        except SA.exc.DBAPIError as exc:
            if attempts >= 0:
                warning(session, exc)
            else:
                warning(session, exc)
        except Exception as e:
            catch_exception(session, e)
    return None
