#!/usr/bin/python3
"""_summary_"""


import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv

if __name__ == "__main__":

    engine = db.create_engine(
        "mysql://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))
    session = sessionmaker(bind=engine)()
    res = session.query(State).order_by(State.id.asc()).all()

    for r in res:
        print(f"{r.id}: {r.name}")
