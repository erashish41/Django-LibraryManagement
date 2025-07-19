from django.urls import path
from library.views import BookListView, LibraryBranchListView, MemberListView, IssuedBookListView, AuthorListView, PublisherListView

urlpatterns = [
    path('books/',BookListView.as_view(),name='book_list'),
    path('branches/',LibraryBranchListView.as_view(),name='branch_list'),
    path('members/',MemberListView.as_view(),name='member_list'),
    path('issuedbooks/',IssuedBookListView.as_view(),name='issuedbooks_list'),
    path('authors/',AuthorListView.as_view(),name='authors_list'),
    path('publishers/',PublisherListView.as_view(),name='publisher_list'),
]