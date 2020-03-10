from django.urls import path
from .views import (
    ContactView, CustomerView,
    ContactDetail, CustomerDetail,
    ContactCreate, CustomerCreate,
    ContactUpdate, CustomerUpdate,
    ContactDelete, CustomerDelete
    )
from . import views


urlpatterns = [
    path('post/', ContactView.as_view(), name='adminview'),

    path('post/search', views.search, name='search'),

    # path('post/chart', IndexView.as_view(), name='chart-view'),

    path('post/<int:pk>/', ContactDetail.as_view(), name='contact-detail'),

    path('post/<int:pk>/customer', CustomerDetail.as_view(), name='customer-detail'),

    path('post/<int:pk>/update/', ContactUpdate.as_view(), name='contact-update'),

    path('post/<int:pk>/update/customer', CustomerUpdate.as_view(), name='customer-update'),

    path('post/<int:pk>/delete/', ContactDelete.as_view(), name='contact-delete'),

    path('post/<int:pk>/delete/customer', CustomerDelete.as_view(), name='customer-delete'),

    path('post/new/', ContactCreate.as_view(), name='contact-create'),

    path('post/new/customer', CustomerCreate.as_view(), name='customer-create'),

    # path('post/', views.adminview, name='adminview')

]
