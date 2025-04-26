from django.contrib import admin
from django.urls import path
from menu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.page_view, name='home'),
    path('<path:page_name>/', views.page_view, name='page'),
]
