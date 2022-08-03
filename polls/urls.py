from django.urls import path
from . import views
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact_us, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('setting/', views.setting, name='setting'),
    path('panel/', views.panel, name='panel'),
    path('course/add', views.add_course, name='add_course'),
    path('course/all', views.AllCoursesView.as_view(), name='all_course')
]
