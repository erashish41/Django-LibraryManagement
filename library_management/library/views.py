from django.shortcuts import render
from django.urls import reverse_lazy
from library.models import Book, LibraryBranch, Member, IssuedBook, Author, Publisher
from library.form import (BookCreateForm, LibraryBranchCreateForm, MemberCreateForm, IssuedBookCreateForm,
                          AuthorCreateForm,PublisherCreateForm)
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class BookListView(SuccessMessageMixin,CreateView,ListView):
    model = Book
    form_class = BookCreateForm
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 10
    success_url = reverse_lazy('book_list')
    success_message = "New Book successfully added"
    
class LibraryBranchListView(SuccessMessageMixin,CreateView,ListView):
    model = LibraryBranch
    template_name = 'branches/library_branches_list.html'
    context_object_name = 'branches'
    paginate_by = 10
    form_class = LibraryBranchCreateForm
    success_url = reverse_lazy('branch_list')
    success_message = "New Library Branch successfully added"
    
class MemberListView(SuccessMessageMixin,CreateView,ListView):
    model = Member
    template_name = 'members/member_list.html'
    context_object_name = 'members'
    paginate_by = 10
    form_class = MemberCreateForm
    success_url = reverse_lazy('member_list')
    success_message = "New Member successfully added"
    
    # i want member default
    def get_initial(self):
        data_fixed = super().get_initial()

        
class IssuedBookListView(SuccessMessageMixin,CreateView,ListView):
    model = IssuedBook
    template_name = 'issuedbooks/issued_book_list.html'
    context_object_name = 'issuedbooks'
    paginate_by = 10
    form_class = IssuedBookCreateForm
    success_url = reverse_lazy('issuedbooks_list')
    success_message = "New Issued Books successfully added"
    
class AuthorListView(SuccessMessageMixin,CreateView,ListView):
    model = Author
    template_name = 'authors/author_list.html'
    context_object_name = 'authors'
    paginate_by = 10
    form_class = AuthorCreateForm
    success_url = reverse_lazy('authors_list')
    success_message = "New Author successfully added"
    
class PublisherListView(SuccessMessageMixin,CreateView,ListView):
    model = Publisher
    template_name = 'publishers/publisher_list.html'
    context_object_name = 'publishers'
    paginate_by = 10
    form_class = PublisherCreateForm
    success_url = reverse_lazy('publisher_list')
    success_message = "New Publisher successfully added"
    
