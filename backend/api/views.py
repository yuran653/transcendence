from django.shortcuts import render
from django.http import JsonResponse
from psycopg2 import connect
from os import environ

def list_databases(request):
    conn = connect(
        dbname=environ['POSTGRES_DB'],
        user=environ['POSTGRES_USER'],
        password=environ['POSTGRES_PASSWORD'],
        host='postgres',
        port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
    databases = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return JsonResponse({'databases': databases})

def index(request):
    return render(request, 'index.html')
