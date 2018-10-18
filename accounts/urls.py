from django.urls import path
from accounts import views
import products

urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', products.views.home, name='home'),


]