from django.urls import path
from Familiares.views import *
urlpatterns = [
    path('', inicio, name='FamiliaresInicio'),
    path('info/', familiares, name='FamiliaresInfo'),
    path('about/', about, name= 'About'),   
    path('herencias/', herencias, name='Herencias'),
    path('Formularios', Formularios, name='Formularios'),
    path('CursoFormulario/', cursoFormulario, name='CursoFormulario')
]

#urlpatterns = patterns('',
#    url(r'', include('external_urls.urls')), 
#)