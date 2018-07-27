from auto import views
from django.conf.urls import *

app_name = 'auto'

urlpatterns = [
    url(r'', views.index, name='index'),
    url(r'^meta/', views.display_meta, name='meta'),
]


