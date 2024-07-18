# db_manager/views.py
from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse
from decouple import config

def database_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT datname FROM pg_database;")
        databases = cursor.fetchall()
    return render(request, 'database_list.html', {'databases': databases})

def create_database(request):
    if request.method == 'POST':
        db_name = request.POST.get('db_name')
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE {db_name};")
            return redirect('database_list')
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")
    return render(request, 'create_database.html')
