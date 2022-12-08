from django.urls import path

from . import views


"""url for view functions"""

urlpatterns = [
    path('', views.index, name='index'),
    path('api/addItems/', views.addItems_api),
    path('signup/', views.signup_page, name="signup"),
    #path('login/', views.login_page, name="login" ),
]