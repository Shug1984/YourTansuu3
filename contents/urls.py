from django.urls import path

from .views import (itemcreateview, itemcreatecompleteview)

urlpatterns = [
    path('item-create/', itemcreateview, name='item_create'),
    path('item-create-complete/', itemcreatecompleteview, name='item_create_complete'),
]