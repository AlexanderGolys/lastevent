
from django.contrib import admin
from django.urls import path, include
from basic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home page"),
    path('account/', include('django.contrib.auth.urls')),
    path('logged/', views.logged_home, name="logged home"),
    path('create_obit/', views.obit_form, name="create obit"),
    path('search_obit/', views.search_obit, name='search obit'),
    path('obit/<int:id>', views.obit_detail, name='obits details'),
    path('my_account/', views.my_account, name="my account"),
    path('comp/<int:id>', views.comp_details, name="comp details"),
    path('comp_list', views.comp_list, name="comp list"),
]
