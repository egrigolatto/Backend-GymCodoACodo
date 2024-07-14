from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Date
from datetime import date
from app import app, db   #,ma

# defino las tablas
class Cliente(db.Model):   # la clase Producto hereda de db.Model de SQLAlquemy
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    apellido=db.Column(db.String(100))
    fecha_nacimiento=db.Column(db.Date)
    categoria_plan=db.Column(db.String(100))
    imagen=db.Column(db.String(400))
    def __init__(self,nombre,apellido,fecha_nacimiento, categoria_plan, imagen): #crea el  constructor de la clase
        self.nombre=nombre # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.apellido=apellido
        self.fecha_nacimiento=fecha_nacimiento
        self.categoria_plan=categoria_plan
        self.imagen=imagen

    #  si hay que crear mas tablas , se hace aqui




with app.app_context():
    db.create_all()