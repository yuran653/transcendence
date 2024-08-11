from django.urls import path
from .views import list_databases, index

urlpatterns = [
    path('api/databases/', list_databases, name='list_databases'),
    path('', index, name='index'),
]
