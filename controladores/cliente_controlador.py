from flask import  jsonify,request  #,Flask# del modulo flask importar la clase Flask y los métodos jsonify,request

from app import app, db,ma
from modelos.cliente_modelo import *

class ClienteSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','apellido','fecha_nacimiento','categoria_plan','imagen')

cliente_schema=ClienteSchema()            # El objeto producto_schema es para traer un producto
clientes_schema=ClienteSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto

# crea los endpoint o rutas (json)
@app.route('/clientes',methods=['GET'])
def get_Clientes():
    all_clientes=Cliente.query.all()         # el metodo query.all() lo hereda de db.Model
    result=clientes_schema.dump(all_clientes)  # el metodo dump() lo hereda de ma.schema y
                                               # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla
                     # retorna un JSON de todos los registros de la tabla

@app.route('/clientes/<id>',methods=['GET'])
def get_cliente(id):
    cliente=Cliente.query.get(id)
    return cliente_schema.jsonify(cliente)   # retorna el JSON de un producto recibido como parametro


@app.route('/clientes/<id>',methods=['DELETE'])
def delete_cliente(id):
    cliente=Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return cliente_schema.jsonify(cliente)  # me devuelve un json con el registro eliminado

@app.route('/clientes', methods=['POST']) # crea ruta o endpoint
def create_cliente():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    apellido=request.json['apellido']
    fecha_nacimiento=request.json['fecha_nacimiento']
    categoria_plan=request.json['categoria_plan']
    imagen=request.json['imagen']
    new_cliente = Cliente (nombre,apellido, fecha_nacimiento, categoria_plan ,imagen)
    db.session.add(new_cliente)
    db.session.commit() # confirma el alta
    return cliente_schema.jsonify(new_cliente)

@app.route('/clientes/<id>' ,methods=['PUT'])
def update_cliente(id):
    cliente=Cliente.query.get(id)

    cliente.nombre=request.json['nombre']
    cliente.apellido=request.json['apellido']
    cliente.fecha_nacimiento=request.json['fecha_nacimiento']
    cliente.categoria_plan=request.json['categoria_plan']
    cliente.imagen=request.json['imagen']

    db.session.commit()
    return cliente_schema.jsonify(cliente)

@app.route('/')
def bienvenida():
    return "Bienvenidos al backend"   # retorna el JSON de un usuario recibido como parametro