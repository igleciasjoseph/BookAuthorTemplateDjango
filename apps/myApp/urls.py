from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('books/<Book_id>', views.bookid),
    path('authors', views.authors),
    path('authoradd', views.authoradd),
    path('authors/<Author_id>', views.authorid),
    path('bookauthor/<book_id>', views.bookauthor),
    path('authorbook/<author_id>', views.authorbook),
]
