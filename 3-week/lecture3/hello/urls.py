from hello import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>', views.greet, name='greet'),
]