from django.urls import path
from fetch import views

urlpatterns = [
    path('', views.index, name='index'),
    path('today', views.todayMenu, name='todayMenu'),
    path('tomorrow', views.tomorrowMenu, name='tomorrowMenu'),
    path('date/<str:dateString>', views.getMenuByDate, name='MenuByDate')
]