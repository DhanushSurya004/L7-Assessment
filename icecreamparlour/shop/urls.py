from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name=""),
    path('menu',views.menu,name="menu"),

]