from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import (Item, Closet, ItemType, ItemColor, ItemBrand, PurchasePlace, SEASON_CHOICES, OCCASION_CHOICES, ITEM_IMPORTANCE_CHOICES, FAVORITE_LEVEL_CHOICES)
from .forms import (ItemTypeCreateForm, ItemColorCreateForm, ItemBrandCreateForm, PurchasePlaceCreateForm, ClosetCreateForm, ItemCreateForm)


@login_required
def item_type_CreateView(request):
    if request.method == 'POST':
        form = ItemTypeCreateForm(request.POST)
        if form.is_valid():
            item_type = form.save(commit=False)
            item_type.user = request.user
            item_type.save()
            return redirect('item_type_create_complete')
    else:
        form = ItemTypeCreateForm()
    return render(request,'contents/item_category_registration/item_type_create.html', {'form':form})


@login_required
def item_type_CreateCompleteView(request):
    return render(request, 'contents/item_category_registration/item_type_complete.html')


@login_required
def item_color_CreateView(request):
    if request.method == 'POST':
        form = ItemColorCreateForm(request.POST)
        if form.is_valid():
            item_color = form.save(commit=False)
            item_color.user = request.user
            item_color.save()
            return redirect('item_color_create_complete')
    else:
        form = ItemColorCreateForm()
    return render(request,'contents/item_category_registration/item_color_create.html', {'form':form})


@login_required
def item_color_CreateCompleteView(request):
    return render(request, 'contents/item_category_registration/item_color_complete.html')


@login_required
def item_brand_CreateView(request):
    if request.method == 'POST':
        form = ItemBrandCreateForm(request.POST)
        if form.is_valid():
            item_brand = form.save(commit=False)
            item_brand.user = request.user
            item_brand.save()
            return redirect('item_brand_create_complete')
    else:
        form = ItemBrandCreateForm()
    return render(request,'contents/item_category_registration/item_brand_create.html', {'form':form})


@login_required
def item_brand_CreateCompleteView(request):
    return render(request, 'contents/item_category_registration/item_brand_complete.html')


@login_required
def purchase_place_CreateView(request):
    if request.method == 'POST':
        form = PurchasePlaceCreateForm(request.POST)
        if form.is_valid():
            purchase_place = form.save(commit=False)
            purchase_place.user = request.user
            purchase_place.save()
            return redirect('purchase_place_create_complete')
    else:
        form = PurchasePlaceCreateForm()
    return render(request,'contents/item_category_registration/purchase_place_create.html', {'form':form})


@login_required
def purchase_place_CreateCompleteView(request):
    return render(request, 'contents/item_category_registration/purchase_place_complete.html')


@login_required
def closet_CreateView(request):
    if request.method == 'POST':
        form = ClosetCreateForm(request.POST)
        if form.is_valid():
            closet = form.save(commit=False)
            closet.user = request.user
            closet.save()
            return redirect('closet_create_complete')
    else:
        form = ClosetCreateForm()
    return render(request,'contents/closet_registration/closet_create.html', {'form':form})


@login_required
def closet_CreateCompleteView(request):
    return render(request, 'contents/closet_registration/closet_create_complete.html')


@login_required
def item_Createview(request):
    if request.method == 'POST':
        form = ItemCreateForm(request.POST, request.FILES)
        if form.is_valid():
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
        form = ItemCreateForm()
    return render(request,'contents/item_registration/item_create.html', {'form':form})


@login_required
def item_CreateCompleteView(request):
    return render(request, 'contents/item_registration/item_create_complete.html')


@login_required
def item_category_GateView(request):
    return render(request, 'contents/item_registration/item_category_gate.html')






# Create your views here.
