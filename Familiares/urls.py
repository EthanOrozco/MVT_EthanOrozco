from xml.etree.ElementInclude import include
from django.urls import path
from Familiares.views import about, familiares, inicio

urlpatterns = [
    path('', inicio, name='FamiliaresInicio'),
    path('info/', familiares, name='FamiliaresInfo'),
    path('about/', about, name= 'About'),

]

urlpatterns = patterns('',
    url(r'', include('external_urls.urls')), 
)