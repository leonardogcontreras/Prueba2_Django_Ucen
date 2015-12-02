from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^listar/$', views.lista_info, name='info_list'),
    url(r'^update/(?P<pk>\d+)/$', views.update_info, name='info_update'),
]
