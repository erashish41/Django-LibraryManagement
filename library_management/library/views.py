from django.shortcuts import render
from library.models import Book, LibraryBranch, Member, IssuedBook, Author, Publisher
from django.views.generic import ListView


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 10
    
class LibraryBranchListView(ListView):
    model = LibraryBranch
    template_name = 'branches/library_branches_list.html'
    context_object_name = 'branches'
    paginate_by = 10
    
class MemberListView(ListView):
    model = Member
    template_name = 'members/member_list.html'
    context_object_name = 'members'
    paginate_by = 10
    
class IssuedBookListView(ListView):
    model = IssuedBook
    template_name = 'issuedbooks/issued_book_list.html'
    context_object_name = 'issuedbooks'
    paginate_by = 10
    
class AuthorListView(ListView):
    model = Author
    template_name = 'authors/author_list.html'
    context_object_name = 'authors'
    paginate_by = 10
    
class PublisherListView(ListView):
    model = Publisher
    template_name = 'publishers/publisher_list.html'
    context_object_name = 'publishers'
    paginate_by = 10
    
