from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text, DateTime, Boolean, text

Base = declarative_base()

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column('id', Integer, primary_key=True)
    ticket_id = Column(String)
    previous_time_spent = Column(Integer)
    current_time_spent = Column(Integer)

    def __repr__(self):
        return '<Ticket %r>' % (self.ticket_id)
