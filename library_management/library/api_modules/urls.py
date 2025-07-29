from django.urls import path, include
from rest_framework import routers

from library import views
from library.api_modules.views import (
    ListCreateIssuedBook, RetrieveUpdateDestroyIssuedBook,
    ListCreateBook, RetrieveUpdateDestroyBook,
    
    IssuedBookViewSet, BookViewSet
    )

router = routers.SimpleRouter()
router.register(r'issuedbooks',IssuedBookViewSet)
router.register(r'books',BookViewSet)

urlpatterns = [
    path('v2/', include(router.urls)),
    
    path('issuedbooks/',ListCreateIssuedBook.as_view(),name='issuedbook_list'),
    path('issuedbooks/<uuid:pk>/',RetrieveUpdateDestroyIssuedBook.as_view(),name='issuedbook_detail'),
    
    path('issuedbooks/<uuid:issuedbook_pk>/books/',ListCreateBook.as_view(),name='book_list'),
    path('issuedbooks/<uuid:issuedbook_pk>/books/<uuid:pk>/',RetrieveUpdateDestroyBook.as_view(),name='book_detail'),


]
