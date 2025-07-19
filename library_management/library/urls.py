from django.urls import path
from library.views import BookListView, LibraryBranchView, MemberView

urlpatterns = [
    path('books/',BookListView.as_view(),name='book_list'),
    path('branches/',LibraryBranchView.as_view(),name='branch_list'),
    path('members/',MemberView.as_view(),name='member_list'),
]