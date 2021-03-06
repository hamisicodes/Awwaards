from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.dashboard , name = 'dashboard'),
    path('register/', views.register, name='register'),
    path('login/' , auth_views.LoginView.as_view() ,name ='login'),
    path('logout/' , auth_views.LogoutView.as_view(),{"next_page": '/'} ,name ='logout' ),
    path('edit/', views.edit , name='edit'),
    path('profile/', views.profile, name= 'profile'),
    path('profile/<username>', views.get_profile, name= 'get_profile'),
    path('create/', views.create , name='create'),
    path('rate/<int:pk>/', views.rate , name='rate'),
    path('project/<int:pk>/', views.single , name='single'),
    path('searches/' , views.searches , name = 'searches'),

    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)