from django.urls import path
from .views import database_list, create_database

urlpatterns = [
    path('', database_list, name='database_list'),
    path('create/', create_database, name='create_database'),
]
