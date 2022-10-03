from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from ast import Delete
import email
from email.policy import HTTP
from os import stat
from re import I
from django.shortcuts import render
from rest_framework import viewsets,status
from django.contrib.auth.models import User, auth
from Serialization import serializers
from Serialization.models import Users
from Serialization.models import Book
from Serialization.serializers import BookSerializer , UserSerializer
from rest_framework.response import Response

class BookViewSet(viewsets.ViewSet):
    # GET BOOKS
    def list(self,request):
        books = Book.objects.all();
        serializer = BookSerializer(books,many = True);
        return Response(serializer.data,status=status.HTTP_302_FOUND);
    # CREATE BOOKS
    def create(self,request):
        serializer = BookSerializer(data = request.data);
        serializer.is_valid(raise_exception=True);
        serializer.save();
        return Response(serializer.data, status=status.HTTP_201_CREATED);


    # GET BOOK BY ID
    def retrieve(self,request,pk=None):
        if(pk):
            book = Book.objects.get(id=pk);
            serializer = BookSerializer(book);
            return Response(serializer.data,status=status.HTTP_200_OK);
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



    # UPDATE BOOK BY ID
    def update(self,request,pk=None):
        if(pk):
            book = Book.objects.get(id=pk);
            serializer = BookSerializer(instance=book,data=request.data);
            serializer.is_valid(raise_exception=True);
            serializer.save();
            return Response(serializer.data,status=status.HTTP_201_CREATED);
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND);
    
    # DELETE BOOK BY ID
    def destroy(self,request,pk=None):
        if(pk):
            book = Book.objects.get(id=pk);
            book.delete();
            return Response(status=status.HTTP_204_NO_CONTENT);
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND);

class UserViewSet(viewsets.ViewSet):
    # GET LIST OF ALL USER
    def list(self,request):
        users = Users.objects.all();
        serializer = UserSerializer(users,many=True);
        return Response(serializer.data,status=status.HTTP_200_OK);
    # CREATE USER
    def create(self,request):
        serializer = UserSerializer(data= request.data)
        serializer.is_valid(raise_exception=True);
        serializer.save();
        return Response(serializer.data, status=status.HTTP_201_CREATED);
    # GET USER BY ID
    def retrieve(self,request,pk=None):
        user = Users.objects.get(id=pk);
        serializer = UserSerializer(user);
        return Response(serializer.data,status=status.HTTP_200_OK);
    # UPDATE USER BY ID 
    def update(self,request,pk=None):
        if(pk):
            user = Users.objects.get(id=pk);
            serializer = UserSerializer(instance=user,data=request.data);
            serializer.is_valid(raise_exception=True);
            serializer.save();
            return Response(serializer.data,status=status.HTTP_201_CREATED);
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND);
    # DELTE USER BY ID
    def destroy(self,request,pk=None):
        if(pk):
            user = Users.objects.get(id=pk);
            user.delete();
            return Response(status=status.HTTP_204_NO_CONTENT);
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND);
    
    # AUTHENTICATE USER
    def login_user(self,request,pk=None):
        if(pk):
            user = Users.objects.get(username=pk);
            userserializer = UserSerializer(user);
            postserializer = UserSerializer(data=request.data);
            postserializer.is_valid(raise_exception=False);
            print(userserializer.data)
            print(postserializer.data)
            if(userserializer.data['password'] == postserializer.data['password']):
                return Response(status=status.HTTP_202_ACCEPTED);
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED);
        else:
            return Response(status=status.HTTP_204_NO_CONTENT);
            


