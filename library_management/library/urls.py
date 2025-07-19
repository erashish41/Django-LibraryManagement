from django.urls import path
from library.views import BookListView

urlpatterns = [
    path('books/',BookListView.as_view(),name='book_list')
]