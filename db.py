# Script that maps our database objects into easily usable classes in Python
from peewee import *


database = MySQLDatabase('bkidsdb', **{'host': 'bkidsdb.cicx3gg9aylv.us-west-2.rds.amazonaws.com', 'password': '12345678', 'port': 3306, 'user': 'intensetundra'})

# Ignore this
class UnknownField(object):
    pass

# Ignore this
class BaseModel(Model):
    class Meta:
        database = database

# This is our User object with all the attributes it saves
class User(BaseModel):
    user_id = PrimaryKeyField(db_column='user_id')
    messenger_id = CharField(db_column='messenger_id', null=True)
    state = CharField(db_column='state', null=True)
    score = IntegerField(db_column='score', null=True)

    class Meta:
        db_table = 'User'