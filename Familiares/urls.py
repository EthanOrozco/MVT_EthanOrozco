from django.urls import path
from Familiares.views import about, familiares, herencias, inicio

urlpatterns = [
    path('', inicio, name='FamiliaresInicio'),
    path('info/', familiares, name='FamiliaresInfo'),
    path('about/', about, name= 'About'),   
    path('herencias/', herencias),
]

#urlpatterns = patterns('',
#    url(r'', include('external_urls.urls')), 
#)