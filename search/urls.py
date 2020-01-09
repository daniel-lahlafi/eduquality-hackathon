from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
    path('<str:query>/', views.searchView, name='search'),
]