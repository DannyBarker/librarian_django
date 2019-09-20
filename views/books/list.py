import sqlite3
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book
from libraryapp.models import model_factory
from ..connection import Connection

@login_required
def book_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Book)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.isbn,
                b.author,
                b.year_published,
                b.librarian_id,
                b.location_id
            from libraryapp_book b
            """)

            dataset = db_cursor.fetchall()

        template = 'books/list.html'
        context = {
            'all_books': dataset
        }

        return render(request, template, context)

    elif (request.method == 'POST'):
        form_data = request.POST
        if  "actual_method" not in form_data:
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                INSERT INTO libraryapp_book
                (
                    title, author, isbn,
                    year_published, location_id, librarian_id
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (form_data['title'], form_data['author'],
                    form_data['isbn'], form_data['year_published'], form_data["location"], request.user.librarian.id))

            return redirect(reverse('libraryapp:books'))

        if (
                "actual_method" in form_data
                and form_data["actual_method"] == "Add It"
            ):
            form_data = request.POST

            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE libraryapp_book
                SET
                    title = ?,
                    ISBN = ?,
                    author = ?,
                    year_published = ?,
                    librarian_id = ?,
                    location_id = ?
                WHERE id = ?;
                """,
                (form_data['title'], form_data['isbn'], form_data['author'], form_data['year_published'], request.user.librarian.id, form_data["location"], form_data["book_id"]))

            return redirect(reverse('libraryapp:book', args = [form_data["book_id"]]))
