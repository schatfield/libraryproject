from django.urls import path
from django.urls import include, path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    # path('', home, name='home'),
    # path('accounts/', include('django.contrib')),
    path('', book_list, name='home'),
    path('books/', book_list, name='books'),
    # path('books/<int:book_id>/', book_details, name='book'),
    path('book/form', book_form, name='book_form'),
    path('librarians/', list_librarians, name='librarians'),
    path('libraries/', list_libraries, name='libraries'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),

]