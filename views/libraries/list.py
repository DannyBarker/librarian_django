import sqlite3
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import render
from libraryapp.models import Library
from libraryapp.models import model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def library_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Library)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                l.id,
                l.title,
                l.address
            from libraryapp_library l
            """)

            dataset = db_cursor.fetchall()

        template = 'libraries/list.html'
        context = {
            'all_libraries': dataset
        }

        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_library
            (
                title, address
            )
            VALUES (?, ?)
            """,
            (form_data['title'], form_data['address']))

        return redirect(reverse('libraryapp:libraries'))
