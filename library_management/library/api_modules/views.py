from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from library.models import Book, LibraryBranch, Member, IssuedBook, Author, Publisher
from library.api_modules.serializers import IssuedBookSerializer, MemberSerializer, BookSerializer, AuthorSerializer, CategorySerializer, LibraryBranchSerializer, CitySerializer

class ListCreateMember(APIView):
    
    def get(self,request,format=None):
        print(">>>>>.get method called")
        member = Member.objects.all()
        serializer = MemberSerializer(member,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        print(">>>>>.post method called")
        serializer = MemberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(">>>>status>>>>", status)
        print(">>>>status>>>>", serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)