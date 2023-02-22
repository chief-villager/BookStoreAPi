from turtle import title
from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import SessionAuthentication

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    authentication_classes = [SessionAuthentication]


    # def perform_create(self, serializer):
        # title = serializer.validated_data.get("title")
        # author = serializer.validated_data.get("author")

        # serializer.save(title = title,author = author)

    def perform_create(self, serializer):
        return super().perform_create(serializer)



class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"
    authentication_classes = [SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]



    def perform_update(self, serializer):
        return super().perform_update(serializer)


    def perform_destroy(self, instance):
        return super().perform_destroy(instance)










