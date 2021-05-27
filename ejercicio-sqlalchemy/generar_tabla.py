from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///basetaller.db')

Base = declarative_base()


class Mundial(Base):
    __tablename__ = "Mundial"
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    fifa_d_name = Column(String(50))
    country = Column(String(50))
    last_name = Column(String(50))
    first_name = Column(String(50))
    shirt_name = Column(String(50))
    pos = Column(String(5))
    height = Column(Integer)
    caps = Column(Integer)
    goals = Column(Integer)

    def __repr__(self):
        return "Data: Numero:%s FIFA Display Name:%s Pais:%s Apellido:%s Nombre:%s Camiseta:%s Posicion:%s Altura:%s " \
               "Caps:%s Goles:%s\n" % (
                   self.numero,
                   self.fifa_d_name,
                   self.country,
                   self.last_name,
                   self.first_name,
                   self.shirt_name,
                   self.pos,
                   self.height,
                   self.caps,
                   self.goals)


Base.metadata.create_all(engine)
