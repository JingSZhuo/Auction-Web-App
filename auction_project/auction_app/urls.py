from django.urls import path

from . import views


"""url for view functions"""

urlpatterns = [
    path('', views.index, name='index'),
    path('api/addItems/', views.addItems_api),
]