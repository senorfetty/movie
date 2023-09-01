from django.urls import path
from . import views


urlpatterns = [
    path('',views.log, name='log'),
    path('signup/', views.sign, name='sign'),
    path('home/', views.home, name='home'),
    path('activate/<slug:uidb64>/<slug:token>', views.activate, name='activate'),
    path('logout/', views.logout_user, name='logout')
]