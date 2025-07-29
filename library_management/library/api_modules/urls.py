from django.urls import path
from library.api_modules.views import (
    ListCreateIssuedBook, RetrieveUpdateDestroyIssuedBook,
    ListCreateMember, RetrieveUpdateDestroyMember,
    ListCreateBook, RetrieveUpdateDestroyBook,
    ListCreateLibraryBranch, RetrieveUpdateDestroyLibraryBranch
    )

urlpatterns = [
    
    path('issuedbooks/',ListCreateIssuedBook.as_view(),name='issuedbook_list'),
    path('issuedbooks/<uuid:pk>/',RetrieveUpdateDestroyIssuedBook.as_view(),name='issuedbook_detail'),
    
    path('issuedbooks/<uuid:issuedbook_pk>/books/',ListCreateBook.as_view(),name='book_list'),
    path('issuedbooks/<uuid:issuedbook_pk>/books/<uuid:pk>/',RetrieveUpdateDestroyBook.as_view(),name='book_detail'),
    
    # path('librarybranches/',ListCreateLibraryBranch.as_view(),name='branch_list'),
    # path('librarybranches/<uuid:pk>/',RetrieveUpdateDestroyLibraryBranch.as_view(),name='librarybranche_detail'),
    
    
    
    # path('members/',ListCreateMember.as_view(),name='member_list'),
    # path('members/<uuid:pk>/',RetrieveUpdateDestroyMember.as_view(),name='member_detail'),
]
