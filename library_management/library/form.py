from django import forms
from library.models import Book, LibraryBranch, Member, IssuedBook, Author, Publisher

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        
class LibraryBranchCreateForm(forms.ModelForm):
    class Meta:
        model = LibraryBranch
        fields = "__all__"
        
class MemberCreateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"
        
class IssuedBookCreateForm(forms.ModelForm):
    class Meta:
        model = IssuedBook
        fields = "__all__"
        
class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        
class PublisherCreateForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"
        
        