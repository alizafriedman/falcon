from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime, func
from sqlalchemy.ext.declarative import declarative_base, declared_attr
import datetime




class BaseModel(object):
    @declared_attr

    def __tablename__(self):
        return self.__name__.lower()


    def to_dict(self):
        intersection = set(self.__table__.column.keys()) & set(self.FIELDS)
        return dict(map(
            lambda key: (
                key, 
                (
                    lambda value: self.FIELDS[key](value) if value else None
                )
                (getattr(self, key))
            ),
            intersection
        ))


    FIELDS = {}

Base = declarative_base(cls=BaseModel)


class Task(Base):
    id = Column(Integer, primary_key=True)
    task_name = Column(String(50), nullable=False)
    created= Column(DateTime, default = datetime.datetime.utcnow)
    modified = Column(DateTime, default = datetime.datetime.utcnow)


    def ___ref__(self):
        return "<Task(task_name = '%s', is_finished='%s')>" % \ 
        (self.task_name, self.is_finished)



    FIELDS = {
        'task_name': str,
    }

    FIELDS.update(Base.FIELDS)