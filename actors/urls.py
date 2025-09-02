from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name='movie-create-list'),
    path('actors/<int:pk>', views.ActorRetrieveUpdateDestroyView.as_view(), name='movie-detail-list'),
]
