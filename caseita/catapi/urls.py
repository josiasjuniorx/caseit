from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todos', views.todos, name='todos'),
    path('raca/<str:breedid>', views.raca, name='raca'),
    path('temperamento/<str:temperamento>', views.temperamento, name='temperamento'),
    path('origem/<str:origem>', views.origem, name='origem'),
    path('update/<str:breedid>', views.update, name='update'),
    path('create', views.create, name='create'),
    path('categoria/<str:categoryname>', views.categoria, name='categoria'),
]