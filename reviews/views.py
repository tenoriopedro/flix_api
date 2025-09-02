from rest_framework import generics
from reviews.models import Review
from rest_framework.permissions import IsAuthenticated
from reviews.serializers import ReviewSerializer
from project.permissions import GlobalDefaultPermission


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer