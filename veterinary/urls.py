from django.urls import path
from . import views

urlpatterns = [
    path("veterinary_dash/", views.vetdash, name="dash1"),
    path("logout/", views.logoutUser, name="logoutUser"),
    path("vetproducts/", views.vetmyproduct, name="vetproducts"),
    path("add/", views.addproduct, name="addproduct"),
    path('locate/', views.locateFarm, name="locate")
]
