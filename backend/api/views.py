from django.http import JsonResponse
from django.db import connection

def list_databases(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT datname FROM pg_database;")
        databases = cursor.fetchall()
    
    database_list = [db[0] for db in databases]
    if not database_list:
        return JsonResponse({'message': 'No available databases'}, status=404)
    
    return JsonResponse({'databases': database_list})
