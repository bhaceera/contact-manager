from django.urls import path
from .views import (
    ContactView,
    ContactDetail,
    ContactCreate,
    ContactUpdate,
    ContactDelete,
    TrashView,
    TrashDetail,
    TrashUpdate,
    TrashDelete,
    TrashCreate
    )
from . import views

urlpatterns = [
    path('post/', ContactView.as_view(), name='adminview'),
    path('post/search', views.search, name='search'),
    path('post/trash', TrashView.as_view(), name='trashview'),
    path('post/<int:pk>/', ContactDetail.as_view(), name='contact-detail'),
    path('post/<int:pk>/trash', TrashDetail.as_view(), name='trash-detail'),
    path('post/<int:pk>/update/', ContactUpdate.as_view(), name='contact-update'),
    path('post/<int:pk>/trash/update/', TrashUpdate.as_view(), name='trash-update'),
    path('post/<int:pk>/delete/', ContactDelete.as_view(), name='contact-delete'),
    path('post/<int:pk>/trash/delete/', TrashDelete.as_view(), name='trash-delete'),
    path('post/new/', ContactCreate.as_view(), name='contact-create'),
    path('post/trash/add', TrashCreate.as_view(), name='trash-create'),
    # path('post/', views.adminview, name='adminview')

]
