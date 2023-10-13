from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('film/<slug:slug>/', views.film_detail, name='film_detail'),
    path('member-area/', views.member_area, name='member_area'),
    path('member-area/add_comment',
         views.add_comment, name='add_comment'),
    path('member-area/delete_comment/<slug:slug>/<int:comment_id>',
         views.delete_comment, name='delete_comment'),
    path('member-area/edit_comment/<int:comment_id>',
         views.edit_comment, name='edit_comment'),
    path('member-area/add_score',
         views.add_score, name='add_score'),
    path('member-area/delete_score/<int:score_id>',
         views.delete_score, name='delete_score'),
]
