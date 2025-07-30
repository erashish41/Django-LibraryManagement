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
    
    path('api/issuedbooks/',ListCreateIssuedBook.as_view(),name='api_issuedbook_list'),
    path('api/issuedbooks/<uuid:pk>/',RetrieveUpdateDestroyIssuedBook.as_view(),name='api_issuedbook_detail'),
    
    path('api/issuedbooks/<uuid:issuedbook_pk>/books/',ListCreateBook.as_view(),name='api_book_list'),
    path('api/issuedbooks/<uuid:issuedbook_pk>/books/<uuid:pk>/',RetrieveUpdateDestroyBook.as_view(),name='api_book_detail'),


]
