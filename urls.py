from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    url(r'^$', home, name='home'),
    path('books', book_list, name='books'),
    path('book/form', book_form, name='book_form'),
    path('books/<int:book_id>/', book_details, name="book"),
    path('librarians', list_librarians, name='librarians'),
    path('librarian/<int:librarian_id>/', librarian_details, name='librarian'),
    path('libraries', library_list, name='libraries'),
    path('library/<int:library_id>/', library_details, name='library'),
    path('library/form', library_form, name='library_form'),
    path('logout/', logout_user, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]
