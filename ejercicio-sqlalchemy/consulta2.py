from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,or_

from generar_tabla import Mundial

engine = create_engine('sqlite:///basetaller.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar todos los jugadores, ordenados por la estatura.
consulta2 = session.query(Mundial).order_by(Mundial.height.desc()).all()

print(consulta2)