from django.db import models


# Create your models here.

class Jvconsultacontroller(models.Model):
    id_tipo_sensor = models.IntegerField(primary_key=True, null=False)
    sensor = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    fecha_inicio = models.DateField(null=True)


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Tipo_sensor(models.Model):
    id_tipo_sensor = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=32, null=True)

class Componente(models.Model):
    id_componente = models.IntegerField(primary_key=True)


class Ubicacion(models.Model):
    id_ubicacion = models.IntegerField(primary_key=True)


class Servicio(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100, null=True)


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)

class Sensor(models.Model):
    id_sensor = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=32)
    fabricante = models.CharField(max_length=32)
    id_tipo_sensor = models.ForeignKey(Tipo_sensor, on_delete=models.CASCADE)
    id_componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    idsentilo = models.IntegerField(null=False)
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100, null=True)
    modelo = models.CharField(max_length=255, null=True)
    num_serie = models.CharField(max_length=255, null=True)
    mac = models.CharField(max_length=255, null=True)
    tipo_energia = models.CharField(max_length=255, null=True)
    tipo_conexion = models.CharField(max_length=255, null=True)
    productor = models.CharField(max_length=255, null=True)
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    grupos = models.CharField(max_length=255, null=False)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)





