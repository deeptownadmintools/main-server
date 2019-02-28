from flask_sqlalchemy import Model
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declared_attr

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


class IdModel(Model):
    @declared_attr
    def id(self):
        for base in self.__mro__[1:-1]:
            if getattr(base, '__table__', None) is not None:
                type = sa.ForeignKey(base.id)
                break
        else:
            type = sa.BigInteger

        return sa.Column(type, primary_key=True)

    @classmethod
    def getById(cls, id):
        entity = cls.query.filter_by(id=id).first()
        return entity