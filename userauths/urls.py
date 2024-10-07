from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.register, name="signup"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="login"),
]
