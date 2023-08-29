from sqlalchemy import Column, DateTime, FetchedValue, Integer, String
from sqlalchemy.sql.sqltypes import  BigInteger
from api.ext.database import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'BPM'}

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(150), nullable=False)
    coins_qty = Column(BigInteger, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=FetchedValue())
    updated_at = Column(DateTime, nullable=True, server_default=FetchedValue())
    deleted_at = Column(DateTime, nullable=True)
    is_active = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'coins_qty': self.coins_qty,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'deleted_at': self.deleted_at,
            'is_active': self.is_active
        }
