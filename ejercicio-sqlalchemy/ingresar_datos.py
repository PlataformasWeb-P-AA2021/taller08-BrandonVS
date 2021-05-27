from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tabla import Mundial
import csv

engine = create_engine('sqlite:///basetaller.db')

Session = sessionmaker(bind=engine)
session = Session()

archivo = open('data/mundial2018.csv', 'r', encoding='utf-8')

archivo_csv = csv.reader(archivo, delimiter='|')

next(archivo_csv)

for d in archivo_csv:
    print(d)
    d = Mundial(numero=int(d[0]), fifa_d_name=d[1], country=d[2], last_name=d[3], first_name=d[4], shirt_name=d[5],
             pos=d[6], height=int(d[7]), caps=int(d[8]), goals=int(d[9]))
    session.add(d)
session.commit()
