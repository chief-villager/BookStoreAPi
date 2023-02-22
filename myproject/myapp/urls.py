from django.urls import path
from . import views

urlpatterns = [

    path('', views.BookListCreateView.as_view()),
    path('<int:pk>/update/', views.BookRetrieveUpdateDestroyView.as_view()),
    path('<int:pk>/delete/', views.BookRetrieveUpdateDestroyView.as_view()),
    path('<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view()),



    ]