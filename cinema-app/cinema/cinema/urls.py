from django.contrib import admin
from django.urls import path
from app.views import MovieListView, MovieView, BaseView, current_version


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view()),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<slug:slug>/', MovieView.as_view(), name='movie-detail'),
    path('version/', current_version, name='version'),
]
