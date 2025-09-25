from rest_framework import generics, views, response, status
from movies. models import Movie
from rest_framework.permissions import IsAuthenticated
from movies.serializers import MovieModelSerializer, MovieListDetailSerializer
from project.permissions import GlobalDefaultPermission
from django.db.models import Count, Avg
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self, request):

        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values(
            'genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(
            avg_stars=Avg('stars'))['avg_stars']

        data = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(
                average_stars, 1
            ) if average_stars else 0,
        }

        return response.Response(
            data=data,
            status=status.HTTP_200_OK,
        )
