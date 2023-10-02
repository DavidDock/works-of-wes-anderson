from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name='home'),
    path('film/<slug:slug>/', views.FilmDetail, name='film_detail'),
    path('member-area/', views.MemberArea, name='member_area'),
    path('member-area/add_comment/<slug:slug>',
         views.AddComment, name='add_comment'),

]
