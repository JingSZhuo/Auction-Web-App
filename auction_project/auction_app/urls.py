from django.urls import path

from . import views


"""url for view functions"""

urlpatterns = [
    path('', views.index, name='index'),
    path('api/addItems/', views.addItems_api),
    
    #Authentication
    path('signupPage/', views.signup_view, name="signup"),
    path('loginPage/', views.login_view, name="login" ),
    path('redirect/', views.redirect_page, name="testing_redirect"),
    path('logout/', views.logout_page, name="logout"),
    
    #api_json
    path('api/usertest_api',views.usertest_api),
    path('api/useremail_api',views.useremail_api),
    path('api/userdob_api',views.userdob_api),
    path('api/profilepicture', views.profile_change),

    #login_only_pages
    path('hidden/', views.hidden_page, name="hidden"),
    path('fetchuser/', views.display_profile)
]