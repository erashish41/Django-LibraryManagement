from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from library.models import Book, LibraryBranch, Member, IssuedBook, Author, Publisher
from library.form import (BookCreateForm, LibraryBranchCreateForm, MemberCreateForm, IssuedBookCreateForm,
                          AuthorCreateForm,PublisherCreateForm)
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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
    
    
class BookDetailView(SuccessMessageMixin,DetailView, UpdateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    success_message = "Book successfully updated"
    
    def get_object(self, queryset = None):
        return get_object_or_404(Book, pk=self.kwargs.get('pk'))
    
    def get_success_url(self):
        return reverse_lazy('book_detail',kwargs={'pk':self.object.pk})
    
    
class BookDeleteView(SuccessMessageMixin,DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
    success_message = 'Book successfully deleted'
    
    
class LibraryBranchListView(SuccessMessageMixin,CreateView,ListView):
    model = LibraryBranch
    template_name = 'branches/library_branches_list.html'
    context_object_name = 'branches'
    paginate_by = 10
    form_class = LibraryBranchCreateForm
    success_url = reverse_lazy('branch_list')
    success_message = "New Library Branch successfully added"
    

class LibraryBranchDetailView(SuccessMessageMixin,DetailView,UpdateView):
    model = LibraryBranch
    form_class = LibraryBranchCreateForm
    template_name = 'branches/library_branch_detail.html'
    context_object_name = 'branch'
    success_message = 'Library Branch successfully updated'
    
    # def get_success_url(self):
    #     return reverse_lazy('branch_list',kwargs = {'pk': self.object.pk})
    
    
class LibraryBranchDeleteView(SuccessMessageMixin,DeleteView):
    model = LibraryBranch
    success_url = reverse_lazy('branch_list')
    success_message = 'Library Branch successfully deleted'

    
class MemberListView(SuccessMessageMixin,CreateView,ListView):
    model = Member
    template_name = 'members/member_list.html'
    context_object_name = 'members'
    paginate_by = 10
    form_class = MemberCreateForm
    success_url = reverse_lazy('member_list')
    success_message = "New Member successfully added"
    
class MemberDetailView(SuccessMessageMixin,DetailView,UpdateView):
    model = Member
    form_class = MemberCreateForm
    template_name = 'members/member_detail.html'
    context_object_name = 'member'
    success_message = "Member successfully updated"
    
    def get_success_url(self):
        return reverse_lazy('member_detail',kwargs={'pk':self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.get_form()
        
        if 'form' not in context:
            context['form'] = form
        return context
    
    
class MemberDeleteView(SuccessMessageMixin,DeleteView):
    model = Member
    success_url = reverse_lazy('member_list')
    success_message = "Member successfully deleted"
    
        
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
    
