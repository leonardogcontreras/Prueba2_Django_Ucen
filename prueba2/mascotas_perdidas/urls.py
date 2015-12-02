from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^listar_perdida/$', views.lista_mascotaperdida, name='mascotaperdida_list'),
    url(r'^listar_encontrada/$', views.lista_mascotaencontrada, name='mascotaencontrada_list'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete_mascotaperdida, name='mascotaperdida_delete'),

]
