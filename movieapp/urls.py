

from django.urls import path
from .views import *

urlpatterns = [
   path('',index,name='index'),
   path('movie/<int:id>/',movie,name='movie'),
   path('movie-detay/<slug:d_slug>/',movieDetail,name='movie-detay'),
   path('search',search,name='search'),
   path('favoriler',favoriler,name='favoriler'),
   path('favori-ekle',favoriEkle,name='favori-ekle')
  
]
