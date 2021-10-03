"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='homepage'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('ticket/<int:ticket_id>/edit/', views.ticket_edit),
    path('ticket/<int:ticket_id>/grab/', views.grab_ticket),
    path('ticket/<int:ticket_id>/return/', views.return_ticket),
    path('ticket/<int:ticket_id>/done/', views.ticket_done),
    path('ticket/<int:ticket_id>/invalid/', views.ticket_invalid),
    path('user/<int:id>/', views.user_detail, name='user_detail'),
    path('user/<int:id>/edit/', views.user_detail),
    path('new/', views.new_ticket),
    path('logout/', views.logout_view),
    path('login/', views.login_page)
]
