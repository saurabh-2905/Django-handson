"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	path("", views.homepage, name="homepage"),
	path("register/", views.register, name="register"),
	path("logout/", views.logout_request, name="logout"),
	path("login/", views.login_request, name="login"),
    path("ip_data", views.ip_data, name="ip_data"),
    path("page1", views.page_one, name="views_page_one"),
    path("page2", views.page_two, name="views_page_two"),
    path("page3", views.page_three, name="views_page_three"),
]
