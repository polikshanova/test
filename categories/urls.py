from django.urls import path
from .views import create, create_tr, edit, delete, index

urlpatterns = [
    path('', index),
    path("create/", create, name='create'),
    path("create_tr/", create_tr, name='create_tr'),
    path("edit/<int:id>/", edit, name='edit'),
    path("delete/<int:id>/", delete, name='delete'),
]
