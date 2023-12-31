
from app import db
class Clientes(db.Model):
    __tablename__ = "clientes"
    ID_del_cliente = db.Column(db.db.Integer,primary_key=True)
    Nombre_del_cliente = db.Column(db.db.String(50))
    apellido_del_cliente = db.Column(db.db.String(50))
    Correo_electrónico_del_cliente = db.Column(db.String(50))
    Dirección_del_cliente = db.Column(db.db.String(50))
    telefono_cliente = db.Column(db.db.Integer(15))
    Fecha_de_nacimiento = db.Column(db.db.Date)
    Género_del_cliente = db.Column(db.db.Enum("masculino", "femenino"))
    numero_de_telefono_cliente = db.Column(db.Integer(30))
    foto_De_perfil_client = db.Column(db.BLOB)
    contraseña_cliente = db.Column(db.String(16))
    
class Administrador(db.Model):
    __tablename__ = "administrador"
    ID_del_administrador = db.Column(db.Integer,primary_key=True)
    Nombre_del_administrador = db.Column(db.String(50))
    apellido_del_administrador = db.Column(db.String(50))
    Correo_electrónico_del_administrador = db.Column(db.String(50))
    Dirección_del_administrador = db.Column(db.String(50))
    Teléfono_del_administrador = db.Column(db.Integer(15))
    Fecha_de_nacimiento =  db.Column(db.Date)
    Género_del_administrador = db.Column(db.Enum("masculino", "femenino"))
    numero_de_telefono_fijo_administrador = db.Column(db.Integer(10))
    foto_De_perfil_administrador = db.Column(db.BLOB)
    contraseña_administrador = db.Column(db.String(16))
    eps = db.Column(db.String(50))
    
class Empleado(db.Model):
    __tablename = "empleado"
    ID_del_empleado = db.Column(db.Integer,primary_key=True)
    Nombre_del_empleado = db.Column(db.String(50))
    apellido_del_empleado = db.Column(db.String(50))
    Correo_electrónico_del_empleado = db.Column(db.String(50))
    permiso_empleado = db.Column(db.Enum("si", "no"))
    Dirección_del_empleado = db.Column(db.String(50))
    Teléfono_del_empleado =db.Column(db.Integer(15))
    Fecha_de_empleado = db.Column(db.Date)
    Género_del_empleado = db.Column(db.Enum("masculino", "femenino"))
    numero_de_telefono_fijo_empleado = db.Column(db.Integer(10))
    foto_De_perfil_empleado = db.Column(db.BLOB)
    contraseña_empleado = db.Column(db.String(16))
    eps = db.Column(db.String(50))
    
class Proyecto(db.Model):
    __tablename__= "proyectos"
    
    id_proyecto = db.Column(db.Integer,primary_key=True)
    nombre_Del_proyecto = db.Column(db.String(50))
    nombre_del_cliente_de_proyecto = db.Column(db.String(50))
    nombre_empleados_participantes_proyecto = db.Column(db.String(50))
    descripcion_del_proyecto = db.Column(db.String(250))
    material_necesitado_del_proyecto = db.Column(db.String(250))

class Informacion(db.Model):
    __tablename__ = "informacion_general"
    id_info = db.Column(db.Integer,primary_key=True)
    foto_info = db.Column(db.String(50))
    descripcion_info = db.Column(db.String(250))
    nombre_info = db.Column(db.String(50))


