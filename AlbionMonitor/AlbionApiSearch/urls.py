from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.AlbionApiSearchView.as_view(), name='search'),
    path('players/<str:id>', views.PlayerView.as_view(), name='players'),
]

