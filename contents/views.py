import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import (Item, Closet, ItemType, ItemColor, ItemBrand, PurchasePlace, SEASON_CHOICES, OCCASION_CHOICES, ITEM_IMPORTANCE_CHOICES, FAVORITE_LEVEL_CHOICES)
from .forms import (ItemTypeCreateForm, ItemColorCreateForm, ItemBrandCreateForm, PurchasePlaceCreateForm, ClosetCreateForm, ItemCreateForm)
from .utils import decode_base64_file


@login_required
def item_type_CreateView(request):
    item_type_list = ItemType.objects.filter(user_id = request.user)
    if request.method == 'POST':
        form = ItemTypeCreateForm(request.POST)
        if form.is_valid():
            item_type = form.save(commit=False)
            item_type.user = request.user
            item_type.save()
            return redirect('item_type_create_complete')
    else:
        form = ItemTypeCreateForm()
    return render(request,'contents/item_category_registration/item_type_create.html', {'form':form, "item_type_list":item_type_list})


@login_required
def item_type_CreateCompleteView(request):
    return render(request, 'contents/item_category_registration/item_type_complete.html')


@login_required
def item_type_UpdateView(request,pk):
    object_item = ItemType.objects.get(user_id = request.user, pk=pk)
    if request.method == 'POST':
       form = ItemTypeCreateForm(request.POST, instance=object_item)
       if form.is_valid():
           form.save()
           return redirect('item_type_update_complete')
    else:
        form = ItemTypeCreateForm(instance = object_item)
    return render(request, 'contents/item_category_edit/item_type_update.html',{'form':form, 'object_item':object_item})


@login_required
def item_type_UpdateCompleteView(request):
    return render(request, 'contents/item_category_edit/item_type_update_complete.html')


@login_required
def item_type_DeleteView(request,pk):
    object_item = ItemType.objects.get(user_id = request.user, pk=pk)
    if request.method == "POST":
        if request.POST.get('button','') == 'confirm':
            object_item.delete()
            return redirect('item_type_delete_complete')
    
    else:
        return render(request, 'contents/item_category_edit/item_type_delete.html',{'object_item':object_item})


@login_required
def item_type_Delete_CompleteView(request):
    return render(request, 'contents/item_category_edit/item_type_delete_complete.html')   


@login_required
def item_color_CreateView(request):
    item_color_list = ItemColor.objects.filter(user_id = request.user)
    if request.method == 'POST':
        form = ItemColorCreateForm(request.POST)
        if form.is_valid():
            item_color = form.save(commit=False)
            item_color.user = request.user
            item_color.save()
            return redirect('item_color_create_complete')
    else:
        form = ItemColorCreateForm()
    return render(request,'contents/item_category_registration/item_color_create.html', {'form':form, "item_color_list":item_color_list })


@login_required
def item_color_CreateCompleteView(request):
    return render(request, 'contents/item_category_registration/item_color_complete.html')


@login_required
def item_color_UpdateView(request,pk):
    object_item = ItemColor.objects.get(user_id = request.user, pk=pk)
    if request.method == 'POST':
       form = ItemColorCreateForm(request.POST, instance=object_item)
       if form.is_valid():
           form.save()
           return redirect('item_color_update_complete')
    else:
        form = ItemColorCreateForm(instance = object_item)
    return render(request, 'contents/item_category_edit/item_color_update.html',{'form':form, 'object_item':object_item})


@login_required
def item_color_UpdateCompleteView(request):
    return render(request, 'contents/item_category_edit/item_color_update_complete.html')


@login_required
def item_color_DeleteView(request,pk):
    object_item = ItemColor.objects.get(user_id = request.user, pk=pk)
    if request.method == "POST":
        if request.POST.get('button','') == 'confirm':
            object_item.delete()
            return redirect('item_color_delete_complete')
    
    else:
        return render(request, 'contents/item_category_edit/item_color_delete.html',{'object_item':object_item})


@login_required
def item_color_Delete_CompleteView(request):
    return render(request, 'contents/item_category_edit/item_color_delete_complete.html')   


@login_required
def item_brand_CreateView(request):
    item_brand_list = ItemBrand.objects.filter(user_id = request.user)
    if request.method == 'POST':
        form = ItemBrandCreateForm(request.POST)
        if form.is_valid():
            item_brand = form.save(commit=False)
            item_brand.user = request.user
            item_brand.save()
            return redirect('item_brand_create_complete')
    else:
        form = ItemBrandCreateForm()
    return render(request,'contents/item_category_registration/item_brand_create.html', {'form':form, "item_brand_list":item_brand_list })


@login_required
def item_brand_CreateCompleteView(request):
    return render(request, 'contents/item_category_registration/item_brand_complete.html')


@login_required
def item_brand_UpdateView(request,pk):
    object_item = ItemBrand.objects.get(user_id = request.user, pk=pk)
    if request.method == 'POST':
       form = ItemBrandCreateForm(request.POST, instance=object_item)
       if form.is_valid():
           form.save()
           return redirect('item_brand_update_complete')
    else:
        form = ItemBrandCreateForm(instance = object_item)
    return render(request, 'contents/item_category_edit/item_brand_update.html',{'form':form, 'object_item':object_item})


@login_required
def item_brand_UpdateCompleteView(request):
    return render(request, 'contents/item_category_edit/item_brand_update_complete.html')


@login_required
def item_brand_DeleteView(request,pk):
    object_item = ItemBrand.objects.get(user_id = request.user, pk=pk)
    if request.method == "POST":
        if request.POST.get('button','') == 'confirm':
            object_item.delete()
            return redirect('item_brand_delete_complete')
    
    else:
        return render(request, 'contents/item_category_edit/item_brand_delete.html',{'object_item':object_item})


@login_required
def item_brand_Delete_CompleteView(request):
    return render(request, 'contents/item_category_edit/item_brand_delete_complete.html')   


@login_required
def purchase_place_CreateView(request):
    purchase_place_list = PurchasePlace.objects.filter(user_id = request.user)
    if request.method == 'POST':
        form = PurchasePlaceCreateForm(request.POST)
        if form.is_valid():
            purchase_place = form.save(commit=False)
            purchase_place.user = request.user
            purchase_place.save()
            return redirect('purchase_place_create_complete')
    else:
        form = PurchasePlaceCreateForm()
    return render(request,'contents/item_category_registration/purchase_place_create.html', {'form':form, "purchase_place_list": purchase_place_list })


@login_required
def purchase_place_CreateCompleteView(request):
    return render(request, 'contents/item_category_registration/purchase_place_complete.html')


@login_required
def purchase_place_UpdateView(request,pk):
    object_item = PurchasePlace.objects.get(user_id = request.user, pk=pk)
    if request.method == 'POST':
       form = PurchasePlaceCreateForm(request.POST, instance=object_item)
       if form.is_valid():
           form.save()
           return redirect('purchase_place_update_complete')
    else:
        form = PurchasePlaceCreateForm(instance = object_item)
    return render(request, 'contents/item_category_edit/purchase_place_update.html',{'form':form, 'object_item':object_item})


@login_required
def purchase_place_UpdateCompleteView(request):
    return render(request, 'contents/item_category_edit/purchase_place_update_complete.html')


@login_required
def purchase_place_DeleteView(request,pk):
    object_item = PurchasePlace.objects.get(user_id = request.user, pk=pk)
    if request.method == "POST":
        if request.POST.get('button','') == 'confirm':
            object_item.delete()
            return redirect('purchase_place_delete_complete')
    
    else:
        return render(request, 'contents/item_category_edit/purchase_place_delete.html',{'object_item':object_item})


@login_required
def purchase_place_Delete_CompleteView(request):
    return render(request, 'contents/item_category_edit/purchase_place_delete_complete.html')   


@login_required
def closet_CreateView(request):
    closet_list = Closet.objects.filter(user_id = request.user)
    if request.method == 'POST':
        form = ClosetCreateForm(request.POST)
        if form.is_valid():
            closet = form.save(commit=False)
            closet.user = request.user
            closet.save()
            return redirect('closet_create_complete')
    else:
        form = ClosetCreateForm()
    
    item_list = Item.objects.filter(user_id = request.user)
    if request.GET.get('closet'):
        closet = request.GET['closet']
        item_list = item_list.filter(closet=closet)
    
    return render(request,'contents/closet_registration/closet_create.html', {'form':form, "closet_list":closet_list,"item_list":item_list })


@login_required
def closet_CreateCompleteView(request):
    return render(request, 'contents/closet_registration/closet_create_complete.html')


@login_required
def closet_UpdateView(request,pk):
    object_item = Closet.objects.get(user_id = request.user, pk=pk)
    if request.method == 'POST':
       form = ClosetCreateForm(request.POST, instance=object_item)
       if form.is_valid():
           form.save()
           return redirect('closet_update_complete')
    else:
        form = ClosetCreateForm(instance = object_item)
    return render(request, 'contents/closet_edit/closet_update.html',{'form':form, 'object_item':object_item})


@login_required
def closet_UpdateCompleteView(request):
    return render(request, 'contents/closet_edit/closet_update_complete.html')


@login_required
def closet_DeleteView(request,pk):
    object_item = Closet.objects.get(user_id = request.user, pk=pk)
    if request.method == "POST":
        if request.POST.get('button','') == 'confirm':
            object_item.delete()
            return redirect('closet_delete_complete')
    
    else:
        return render(request, 'contents/closet_edit/closet_delete.html',{'object_item':object_item})


@login_required
def closet_Delete_CompleteView(request):
    return render(request, 'contents/closet_edit/closet_delete_complete.html')   


@login_required
def item_category_GateView(request):
    return render(request, 'contents/item_registration/item_category_gate.html')


@login_required
def item_Createview(request):
    if request.method == 'POST':
        form = ItemCreateForm(request.POST, request.FILES)
        if form.is_valid():
            action = request.POST['action']
            if action == 'input':
                return render(request, 'contents/item_registration/item_create.html', {'form':form})
            elif action == 'confirm':
                return render(request,'contents/item_registration/item_create_confirm.html',{'form':form, 'item_image_base64': request.POST.get('item_image_base64'),})
            else:
                item = form.save(commit=False)
                item.item_image = decode_base64_file(request.POST.get('item_image'), request.POST.get('item_image_base64'))
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
def item_ListView(request):
    item_list = Item.objects.filter(user_id = request.user)
    if request.GET.get('closet'):
        closet = request.GET['closet']
        item_list = item_list.filter(closet=closet)

    today = datetime.date.today()

    paginator = Paginator(item_list, 10)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'contents/item_list/item_list.html', {'page_object': page_object,'today':today, "paginator":paginator })


@login_required
def item_DetailView(request, pk):
    object_item = Item.objects.get(user_id= request.user, pk=pk)
    return render(request, 'contents/item_list/item_detail.html', {'object_item':object_item})


@login_required
def item_Updateview(request, pk):
    object_item = Item.objects.get(user_id = request.user, pk=pk)
    if request.method == 'POST':
       form = ItemCreateForm(request.POST, request.FILES, instance=object_item)
       if form.is_valid():
           form.item_image = decode_base64_file(request.POST.get('item_image'), request.POST.get('item_image_base64'))
           form.save()
           return redirect('item_detail', pk=pk)
    else:
        form = ItemCreateForm(instance = object_item)
    return render(request, 'contents/item_edit/item_update.html',{'form':form, 'object_item':object_item})


@login_required
def item_Update_CompleteView(request):
    pass


@login_required
def item_DeleteView(request, pk):
    object_item = Item.objects.filter(user_id = request.user, pk=pk)
    if request.method == "POST":
        if request.POST.get('button', '') == 'confirm':
            return render(request, 'contents/item_edit/item_delete_confirm.html', {'object_item':object_item})
        else:
            object_item.delete()
        return redirect('item_delete_complete')
    
    else:
        return render(request, 'contents/item_edit/item_delete.html', {'object_item':object_item})


@login_required
def item_Delete_CompleteView(request):
    return render(request, 'contents/item_edit/item_delete_complete.html')


@login_required
def closet_ListView(request):
    object_list = Closet.objects.filter(user_id = request.user)

    paginator = Paginator(object_list, 10)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'contents/closet_list/closet_list.html', {'page_object': page_object})













# Create your views here.
