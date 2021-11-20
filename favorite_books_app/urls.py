from django.urls import path
from .import views


urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("login", views.login_user),
    path("books", views.show_all),
    path("books/create", views.create_book),
    path('back', views.back),
    path("books/<int:book_id>", views.show_one),
    path("books/<int:book_id>/update", views.update),
    path("books/<int:book_id>/delete", views.delete),
    path("like/<int:pk>", views,like_book, name="like_post"),
    path("favorite/<int:book_id>", views.favorite),
    path("unfavorite/<int:book_id>", views.unfavorite),
    path("logout", views.logout)
]