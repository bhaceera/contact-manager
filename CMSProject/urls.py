"""CMSProject URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from useraccount import views as useraccount_views
# from contacts import views
# from useraccount import views

# if settings.DEBUG:
#     urlpatterns += patterns('',

    # )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', useraccount_views.register, name='register'),
    path('register/added', useraccount_views.register, name='reghome'),
    path('', auth_views.LoginView.as_view(template_name='useraccount/index.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='useraccount/logout.html'), name='logout'),
    path('user/', include('contacts.urls')),
    # path('404/', views.handler404, name="handler404"),
    # path('500/', views.handler500, name="handler500"),

]
