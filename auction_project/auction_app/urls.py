from django.urls import path

from . import views


"""url for view functions"""

urlpatterns = [
    path('', views.index, name='index'),
    path('api/addItems/', views.addItems_api),
    path('signupPage/', views.signup, name="signup"),
    
    path('login/', views.login_page, name="login" ),
    path('redirect/', views.redirect_page, name="testing_redirect"),
    path('logout/', views.logout_page, name="logout"),
    path('hidden/', views.hidden_page, name="hidden")
]