from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse
from app.models import Movie
from app.serializers import MovieSerializer
from rest_framework import generics


class BaseView(View):
    def get(self, request):
        return redirect('/movies/')


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'slug'


def current_version(request):
    html = "<html><body><h3>Cinema Project - version 0.40.0</h3></body></html>"
    return HttpResponse(html)
