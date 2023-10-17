from django.urls import path
from blog import views


urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("food", views.food, name="food"),
    path("travel", views.travel, name="travel"),
    path("fashion", views.fashion, name="fashion"),
    path("create", views.create, name="create"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("upload", views.upload, name="upload"),
    path("upload2", views.upload2, name="upload2"),    
   
]
