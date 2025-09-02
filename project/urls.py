from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),

    # Token
    path('api/v1/', include('authentication.urls')),

    # CRUD Genres
    path('api/v1/', include('genres.urls')),

    # CRUD Actors
    path('api/v1/', include('actors.urls')),

    # CRUD Movies
    path('api/v1/', include('movies.urls')),

    # CRUD Reviews
    path('api/v1/', include('reviews.urls')),

    
]
