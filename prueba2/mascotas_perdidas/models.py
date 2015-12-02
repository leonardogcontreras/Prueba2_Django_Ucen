from django.db import models
from django.contrib.auth.models import User
from estado.models import Estado
from models import *

class Mascotas_Perdidas(models.Model):
	
	estado=models.ForeignKey(Estado, null=False)
	extraviado=models.BooleanField()
	recompenza=models.IntegerField()
	
	def __unicode__(self):
		return '%s %s %s %s %s %s' % (self.estado.Usuario.username,self.estado.Mascota.nombre, self.estado.Mascota.raza, self.estado.Mascota.color, self.estado.Mascota.sexo, self.estado.Mascota.descripcion)




	 		 	