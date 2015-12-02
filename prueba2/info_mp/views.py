from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Info_MP
#ccbv.co.uk

class Info_View(ListView):
	model = Info_MP
	template_name = 'Info_MP/info_list.html'

lista_info = Info_View.as_view()


class Info_Update(UpdateView):
	model= Info_MP
	fields= ['descripcion']
	template_name = 'Info_MP/info_update.html'
	success_url= reverse_lazy(lista_info)

update_info= Info_Update.as_view()