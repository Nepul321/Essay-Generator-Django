from django.urls import path
from .views import *


urlpatterns = [
   path('', HomeView, name="home"),
   path('essays/', EssayListView, name="essays"),
   path('essays/<str:key>/', EssayView, name="essay"),
   path('essays/<str:key>/delete/', EssayDeleteView, name="essay-delete"),

]