
from django.urls import path, include

urlpatterns = [
    path('', include('favorite_books_app.urls'))
]
