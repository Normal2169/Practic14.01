from django.urls import path, re_path
from hello import views
 
urlpatterns = [
    path('', views.index),
    re_path('^about', views.about, kwargs={"name":"Tom", "age": 38}),
    re_path('contact', views.contact),
]