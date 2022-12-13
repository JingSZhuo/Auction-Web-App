from django.urls import path

from . import views


"""url for view functions"""

urlpatterns = [
    path('', views.index, name='index'),
    path('api/addItems/', views.addItems_api),
    path('signupPage/', views.signup, name="signup"),
    path('api/usertest_api',views.usertest_api),
    path('api/useremail_api',views.useremail_api),
    path('api/userdob_api',views.userdob_api),
    path('login/', views.login_page, name="login" ),
    path('redirect/', views.redirect_page, name="testing_redirect"),
    path('logout/', views.logout_page, name="logout"),
    path('hidden/', views.hidden_page, name="hidden")
]