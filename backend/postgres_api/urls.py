from django.urls import path
from api import views

urlpatterns = [
    path('databases/', views.list_databases, name='list_databases'),
]
