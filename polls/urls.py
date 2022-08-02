from django.urls import path
from . import views
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact_us, name='contact'),
    path('profile/', views.profile, name='profile')
]
