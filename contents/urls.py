from django.urls import path

from .views import ( 
    item_type_CreateView, item_type_CreateCompleteView, item_color_CreateView, item_color_CreateCompleteView, item_brand_CreateView, item_brand_CreateCompleteView,
    purchase_place_CreateView, purchase_place_CreateCompleteView, closet_CreateView, closet_CreateCompleteView, item_Createview, item_CreateCompleteView, item_category_GateView,
    item_ListView
)

urlpatterns = [
    path('item-category-gate/', item_category_GateView, name='item_category_gate'),
    path('item-type-create/', item_type_CreateView, name='item_type_create'),
    path('item-type-create-complete/', item_type_CreateCompleteView, name='item_type_create_complete'),
    path('item-color-create/', item_color_CreateView, name='item_color_create'),
    path('item-color-create-complete/', item_color_CreateCompleteView, name='item_color_create_complete'),
    path('item-brand-create/', item_brand_CreateView, name='item_brand_create'),
    path('item-brand-create-complete/', item_brand_CreateCompleteView, name='item_brand_create_complete'),
    path('purchase-place-create/', purchase_place_CreateView, name='purchase_place_create'),
    path('purchase-place-create-complete/', purchase_place_CreateCompleteView, name='purchase_place_create_complete'),
    path('closet-create/', closet_CreateView, name='closet_create'),
    path('closet-create-complete/', closet_CreateCompleteView, name='closet_create_complete'),
    path('item-create/', item_Createview, name='item_create'),
    path('item-create-complete/', item_CreateCompleteView, name='item_create_complete'),
    path('item-list/', item_ListView, name='item_list'),
]