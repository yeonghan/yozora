from django.contrib import admin
from django.urls import path
#from django.views.generic import ListView, DetailView
from test_woo.views import Test_wooLV, Test_wooDV

urlpatterns = {
    path('admin/', admin.site.urls),

    #class-based views
    path('test_woo/', Test_wooLV.as_view(), name='index'),
    path('test_woo/<int:pk>/', Test_wooDV.as_view, name='detail'),
}