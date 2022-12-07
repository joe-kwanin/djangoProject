from django.urls import path
from . import views

urlpatterns = [
    path("farmManager_dash/", views.dash, name="dash"),
    path("logout/", views.logoutUser, name="logoutUser"),
    path("farmproducts/", views.myproduct, name="farmproduct"),
    path("add/", views.addproduct, name="addproduct"),
    path('edit/<int:pid>', views.edit, name="edit"),
    path('records/', views.recordsGet, name='records'),
    path('chart/', views.chart, name='chart')
]
