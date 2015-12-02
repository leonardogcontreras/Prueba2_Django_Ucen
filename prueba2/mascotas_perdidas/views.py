from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Mascotas_Perdidas
#ccbv.co.uk

class MascotaPerdida_View(ListView):
	model = Mascotas_Perdidas
	fields='__all__'
	template_name = 'Mascotas_Perdidas/mascotaperdida_list.html'

lista_mascotaperdida = MascotaPerdida_View.as_view()


class MascotaEncontrada_View(ListView):
	model = Mascotas_Perdidas
	fields='__all__'
	template_name = 'Mascotas_Encontrada/mascotaencontrada_list.html'

lista_mascotaencontrada = MascotaEncontrada_View.as_view()


class MascotaEncontrada_Delete(DeleteView):
	model= Mascotas_Perdidas
	success_url= reverse_lazy(lista_mascotaperdida)
	fields='__all__'
	template_name= 'Mascotas_Perdidas/mascotaperdida_delete.html'

delete_mascotaperdida= MascotaEncontrada_Delete.as_view()