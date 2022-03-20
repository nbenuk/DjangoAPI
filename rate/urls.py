from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name="rmp-list"),
    path('view/', views.view, name="rmp-view"),
    path('avg/', views.avg, name="rmp-avg"),
    path('register/', views.register, name="rmp-register"),
    path('login/', views.login, name="rmp-login"),
    path('logout/', views.logout_, name="rmp-logout"),
    path('rate/', views.rate, name="rmp-rate"),
]

from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]