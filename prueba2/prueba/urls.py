from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mascota/', include('mascota.urls')),
    url(r'^estado/', include('estado.urls')),
    url(r'^mascotas_perdidas/', include('mascotas_perdidas.urls')),
    url(r'^info_mp/', include('info_mp.urls')),


]
