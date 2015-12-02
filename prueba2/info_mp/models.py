from django.db import models
from django.contrib.auth.models import User
from mascotas_perdidas.models import Mascotas_Perdidas
from models import *

class Info_MP(models.Model):
	 mascota_perdida=models.ForeignKey(Mascotas_Perdidas, null=True)
	 #foto= models.ImageField(upload_to = 'fotos')
	 descripcion = models.TextField(max_length=255, blank=False)	 

	 def __unicode__(self):
	 	return self.mascota_perdida.estado.Mascota.nombre

'''	 def traer_url_fotos(self):
	 	return 'http://localhost:8000/%s' % self.fotos'''