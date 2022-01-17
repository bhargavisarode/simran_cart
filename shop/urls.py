from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="ShopHome"),
path("about/", views.about, name="about"),
path("contact/", views.contact, name="about"),
path("tracker/", views.tracker, name="about"),
path("search/", views.search, name="about"),
path("products/<int:myid>", views.prodView, name="about"),
path("checkout/", views.checkout, name="about"),
]