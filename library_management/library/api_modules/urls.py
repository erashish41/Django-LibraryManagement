from django.urls import path
from library.api_modules.views import ListCreateMember

urlpatterns = [
    path('members/',ListCreateMember.as_view(),name='member_list')
]
