from django.urls import path
from app_user_info import views

app_name = 'app_user_info'

urlpatterns = [
    path('', views.division_view.as_view(), name='home_view'),
    path('districts/', views.district_view.as_view(), name='district_view'),
    path('upazillas/', views.upazilla_view.as_view(), name='upazilla_view'),
    path('users/', views.users_view, name='users'),
    path('search_user/', views.search_user_view, name='search_user'),
]