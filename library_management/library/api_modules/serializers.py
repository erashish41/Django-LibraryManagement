from rest_framework import serializers
from library.models import (IssuedBook, Member, Book, Author, Publisher,
                            Category, LibraryBranch, City)

class IssuedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuedBook
        fields = "__all__"
        
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"
        
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class LibraryBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryBranch
        fields = "__all__"
        
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"