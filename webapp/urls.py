from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.my_login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.my_logout,name='logout'),
    path('record/',views.create_record,name='record'),
    path('view/<int:record_id>/',views.record_view,name='view'),
    path('ubdate/<int:record_id>/',views.ubdate_record,name='ubdate'),
    path('delete/<int:record_id>/',views.delete_record,name='delete'),
    path('search/',views.search,name='search')
]