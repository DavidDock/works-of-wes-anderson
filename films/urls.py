from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name='home'),
    path('<slug:slug>/', views.FilmDetail, name='film_detail')
]
