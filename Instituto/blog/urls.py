from django.urls import path
from . import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('crear/', views.CrearPost.as_view(), name='crear'),
    

]