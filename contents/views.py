from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import (Item, Closet, ItemType, ItemColor, ItemBrand, PurchasePlace, SEASON_CHOICES, OCCASION_CHOICES, ITEM_IMPORTANCE_CHOICES, FAVORITE_LEVEL_CHOICES)
from .forms import (ItemCreateForm, ClosetCreateForm, ItemTypeCreateForm, ItemColorCreateForm, ItemBrandCreateForm, PurchasePlaceCreateForm)


@login_required
def itemcreateview(request):
    if request.method == 'POST':
        form = ItemCreateForm(request.POST, request.FILES)
        if form.is_valid():
            ITEM_TYPE = request.POST.get['item_type']
            Item_Type_Object = ItemType(item_type=ITEM_TYPE)
            Item.item_type = Item_Type_Object

            action = request.POST['action']
            if action == 'input':
                return render(request, 'contents/item_registration/item_create.html', {'form':form})
            elif action == 'confirm':
                return render(request,'contents/item_registration/item_create_confirm.html',{'form':form})
            else:
                item = form.save(commit=False)
                form.item_type = Item_Type_Object.save()
                item.user = request.user
                item.save()
                return redirect('item_create_complete')
    else:
        form = ItemCreateForm()
    return render(request,'contents/item_registration/item_create.html', {'form':form})


@login_required
def itemcreatecompleteview(request):
    return render(request, 'contents/item_registration/item_create_complete.html')


@login_required
def ItemTypeCreateView(request):
    if request.method == 'POST':
        form = ItemTypeForm(request.POST)
        if form.is_valid():
            closet = form.save(commit=False)
            closet.user = request.user
            closet.save()
            return redirect('itemtype_create_complete')
    else:
        form = ItemTypeForm()
    return render(request,'contents/closet_create.html', {'form':form})


@login_required
def ItemTypeCreateCompleteView(request):
    return render(request, 'contents/itemtype_create_complete.html')


# Create your views here.
