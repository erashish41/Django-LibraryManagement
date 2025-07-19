from django.shortcuts import render
from library.models import Book, LibraryBranch
from django.views.generic import ListView


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 10
    
class LibraryBranchView(ListView):
    model = LibraryBranch
    template_name = 'branches/library_branches.html'