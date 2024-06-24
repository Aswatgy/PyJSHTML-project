from django.urls import path
from . import views
urlpatterns=[
    path('',views.register), 
    path('login/',views.login), 
    path('login/', views.login_process),
    path('api/mock_login/', views.mock_api_login),
   
    #path()
]