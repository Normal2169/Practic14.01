from django.urls import path, re_path
from hello import views
 
urlpatterns = [
    path('', views.defolt),
    path('index', views.index),
    path('about', views.about, kwargs={"name":"Tom", "age": 38}),
    path('contact', views.contact),
    path("user", views.user),
    path("user/<name>", views.user),
    path("user/<name>/<int:age>", views.user),
]