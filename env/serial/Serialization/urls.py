from django.contrib import admin
from django.urls import path
from Serialization.views import UserViewSet
from Serialization.views import BookViewSet

urlpatterns = [
    # READ , CREATE
    path('books/', BookViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
    # READ , UPDATE, DELETE
    path('books/<str:pk>', BookViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
    # READ,CREATE
    path('users/', UserViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
    # READ , UPDATE, DELETE
    path('users/<str:pk>', BookViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
    # AUTHENTICATE
    path('login/<str:pk>', UserViewSet.as_view({
        'post':'login_user'
    })),
]