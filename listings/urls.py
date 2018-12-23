from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'), # living path blank ('') is the same as /listings
    path('<int:listing_id>', views.listing, name='listing'), # here we add a parameter to path ( /listings/id)
    path('search', views.search, name='search')
]