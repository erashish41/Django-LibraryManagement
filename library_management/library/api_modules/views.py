from rest_framework import generics
from django.shortcuts import get_object_or_404

from library.models import Book, LibraryBranch, Member, IssuedBook, Author, Publisher
from library.api_modules.serializers import IssuedBookSerializer, MemberSerializer, BookSerializer, AuthorSerializer, CategorySerializer, LibraryBranchSerializer, CitySerializer


class ListCreateIssuedBook(generics.ListCreateAPIView):
    queryset = IssuedBook.objects.all()
    serializer_class = IssuedBookSerializer
    
class RetrieveUpdateDestroyIssuedBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = IssuedBook.objects.all()
    serializer_class = IssuedBookSerializer

class ListCreateMember(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
class RetrieveUpdateDestroyMember(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    

class ListCreateBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return self.queryset.filter(issued_records__id = self.kwargs.get('issuedbook_pk'))
    
    def perform_create(self, serializer):
        branch = get_object_or_404(LibraryBranch, pk= self.kwargs.get('issuedbook_pk'))
        serializer.save(library_branch=branch)
    
class RetrieveUpdateDestroyBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_object(self):
        return get_object_or_404(self.get_queryset(),
                                issued_records__id = self.kwargs.get('issuedbook_pk'),
                                pk = self.kwargs.get('pk'))

class ListCreateLibraryBranch(generics.ListCreateAPIView):
    queryset = LibraryBranch.objects.all()
    serializer_class = LibraryBranchSerializer
    
class RetrieveUpdateDestroyLibraryBranch(generics.RetrieveUpdateDestroyAPIView):
    queryset = LibraryBranch.objects.all()
    serializer_class = LibraryBranchSerializer