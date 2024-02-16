from django.urls import path
from .views import *

urlpatterns = [
    path('', BookListAPI, name='BookListAPI'),
    path('BookDetailAPI/<int:blog_id>', BookDetailAPI, name='BookDetailAPI'),
]
