from django.urls import path
from . import views
from django.conf.urls import include

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("", include("django.contrib.auth.urls"))
]