from django.db import models

# Create your models here.

class Jvconsultacontroller (models.Model):
    id_tipo_sensor=models.IntegerField (primary_key=True, null=False)
    sensor=models.CharField (max_length=10)
    descripcion=models.CharField (max_length=50)
    fecha_inicio=models.DateField (null=True)


class Question (models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

class Choice (models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
