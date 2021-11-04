import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import ItemType, ItemColor, ItemBrand, PurchasePlace, Closet, Item, FAVORITE_LEVEL_CHOICES, ITEM_IMPORTANCE_CHOICES, SEASON_CHOICES, OCCASION_CHOICES
from .forms import ClosetForm, ItemForm


@login_required
def itemcreateview(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            Item= form.cleaned_data['item_type ']
            ItemObject = ItemType(item_type =Item)
            ItemObject.save()
            action = request.POST['action']
            if action == 'input':
                return render(request, 'contents/item_registration/item_create.html', {'form':form})
            elif action == 'confirm':
                return render(request,'contents/item_registration/item_create_confirm.html',{'form':form})
            else:
                item = form.save(commit=False)
                item.user = request.user
                item.save()
                return redirect('item_create_complete')
    else:
        form = ItemForm()
    return render(request,'contents/item_registration/item_create.html', {'form':form})


@login_required
def itemcreatecompleteview(request):
    return render(request, 'contents/item_registration/item_complete.html')


"""
Item= form.cleaned_data['item_type ']
ItemObject = ItemType(item_type =Item)
ItemObject.save()
"""

# Create your views here.
