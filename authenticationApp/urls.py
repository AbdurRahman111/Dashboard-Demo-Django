from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_function, name="signup_function"),
    path('login/', views.login_function, name="login_function"),
    path('logout/', views.logout_function, name='logout_function'),
]