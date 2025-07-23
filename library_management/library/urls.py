from django.urls import path
from library.views import (BookListView, BookDetailView, BookDeleteView, LibraryBranchListView, LibraryBranchDetailView, LibraryBranchDeleteView,
                           MemberListView, MemberDetailView, MemberDeleteView, IssuedBookListView, AuthorListView, PublisherListView,
                            )

urlpatterns = [
    path('books/',BookListView.as_view(),name='book_list'),
    path('books/<uuid:pk>/',BookDetailView.as_view(),name='book_detail'),
    path('books/<uuid:pk>/delete',BookDeleteView.as_view(),name='book_delete'),
    
    path('branches/',LibraryBranchListView.as_view(),name='branch_list'),
    path('branch/<uuid:pk>',LibraryBranchDetailView.as_view(),name='branch_detail'),
    path('branch/<uuid:pk>/delete',LibraryBranchDeleteView.as_view(),name='branch_delete'),
    
    path('members/',MemberListView.as_view(),name='member_list'),
    path('members/<uuid:pk>/',MemberDetailView.as_view(),name='member_detail'),
    path('members/<uuid:pk>/delete',MemberDeleteView.as_view(),name='member_delete'),
    
    path('issuedbooks/',IssuedBookListView.as_view(),name='issuedbooks_list'),
    path('authors/',AuthorListView.as_view(),name='authors_list'),
    path('publishers/',PublisherListView.as_view(),name='publisher_list'),
]