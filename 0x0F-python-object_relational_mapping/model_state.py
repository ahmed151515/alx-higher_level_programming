#!/usr/bin/python3
"""_summary_"""

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()


class State(base):
    """_summary_

    Args:
        base (_type_): _description_
    """
    __tablename__ = "states"

    id = db.Column("id", db.Integer, primary_key=True,
                   autoincrement=True, nullable=False
                   )
    name = db.Column("name", db.String(128), nullable=False)
