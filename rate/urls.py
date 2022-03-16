from django.urls import path
from . import views

from django.urls import include

urlpatterns = [
    path('', views.home, name="rmp-home"), 
    # rmp-home
    path('about/', views.about, name="rmp-about"), 
    path('list/', views.list, name="rmp-list"),
    path('view/', views.view, name="rmp-view"),
    path('avg/', views.avg, name="rmp-avg"),
    path('register/', views.register, name="rmp-register"),
    path('login/', views.login, name="rmp-login"),
    path('logout/', views.logout_, name="rmp-logout"),
    path('rate/', views.rate, name="rmp-rate"),
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))

]
from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]