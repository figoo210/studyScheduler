from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

db = SQLAlchemy()



def model_to_dict(model):
    return {column.key: getattr(model, column.key) for column in sqlalchemy.inspect(model).mapper.column_attrs}
