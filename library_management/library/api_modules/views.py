from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from rest_framework import mixins

from django.shortcuts import get_object_or_404


from library.models import Book, LibraryBranch, Member, IssuedBook, Author, Publisher
from library.api_modules.serializers import IssuedBookSerializer, MemberSerializer, BookSerializer, AuthorSerializer, CategorySerializer, LibraryBranchSerializer, CitySerializer


class ListCreateIssuedBook(generics.ListCreateAPIView):
    queryset = IssuedBook.objects.all()
    serializer_class = IssuedBookSerializer
    
class RetrieveUpdateDestroyIssuedBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = IssuedBook.objects.all()
    serializer_class = IssuedBookSerializer

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
        
class ListCreateMember(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
class RetrieveUpdateDestroyMember(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
# for ViewSet
class IssuedBookViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions)
    queryset = IssuedBook.objects.all()
    serializer_class = IssuedBookSerializer
    
    @action(methods=['get'],detail=True)
    def book(self,request,pk=None):
        self.pagination_class.page_size = 1
        books = BookSerializer.object.filter(book_id='pk')
        
        page = self.paginate_queryset(books)
        
        if page is not None:
            serializer = BookSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        issued_book = self.get_object()
        serializer = BookSerializer(books,many=True)
        
        return Response(serializer.data)
    
class BookViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    