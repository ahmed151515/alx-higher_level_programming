#!/usr/bin/python3
"""_summary_"""

import sqlalchemy as db


base = db.ext.declarative_base()


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

    def __init__(self, id: int, name: str):
        """_summary_

        Args:
            id (int): _description_
            name (str): _description_
        """
        self.id = id
        self.name = name
