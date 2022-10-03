from dataclasses import fields
from rest_framework import serializers
from Serialization.models import Users
from Serialization.models import Book;
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book;
        fields = '__all__';

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users;
        fields = ['username','email','password'];
    
