from django import forms
from django.conf import settings

from .models import (Item, Closet, ItemType, ItemColor, ItemBrand, PurchasePlace, SEASON_CHOICES, OCCASION_CHOICES, ITEM_IMPORTANCE_CHOICES, FAVORITE_LEVEL_CHOICES)

MONTHS = {
    1: '1月', 2: '2月', 3: '3月', 4: '4月',
    5: '5月', 6: '6月', 7: '7月', 8: '8月',
    9: '9月', 10: '10月', 11: '11月', 12: '12月'
}


class ItemTypeCreateForm(forms.ModelForm):

    class Meta:
        model = ItemType
        fields = ('item_type',)
        labels = {'item_type':'アイテム種類'}
    
    def clean_item_type(self):
        item_type = self.cleaned_data['item_type']
        if item_type:
            item_type_number = ItemType.objects.filter(item_type=item_type).count()
            if item_type_number > settings.ITEM_TYPE_MAX:
                self.add_error('item_type',f"アイテム種類に設定出来る件数は{settings.ITEM_TYPE_MAX}件までです。")
        return item_type


class ItemColorCreateForm(forms.ModelForm):

    class Meta:
        model = ItemColor
        fields = ('item_color',)
        labels = {'item_color':'アイテムカラー'}
    
    def clean_item_color(self):
        item_color = self.cleaned_data['item_color']
        if item_color:
            item_color_number = ItemColor.objects.filter(item_color=item_color).count()
            if item_color_number > settings.ITEM_COLOR_MAX:
                self.add_error('item_color',f"アイテムカラーに設定出来る件数は{settings.ITEM_COLOR_MAX}件までです。")
        return item_color


class ItemBrandCreateForm(forms.ModelForm):

    class Meta:
        model = ItemBrand
        fields = ('item_brand',)
        labels = {'item_brand':'ブランド名'}
    
    def clean_item_brand(self):
        item_brand = self.cleaned_data['item_brand']
        if item_brand:
            item_brand_number = ItemBrand.objects.filter(item_brand=item_brand).count()
            if item_brand_number > settings.ITEM_BRAND_MAX:
                self.add_error('item_brand',f"ブランドに設定出来る件数は{settings.ITEM_BRAND_MAX}件までです。")
        return item_brand


class PurchasePlaceCreateForm(forms.ModelForm):

    class Meta:
        model = PurchasePlace
        fields = ('purchase_place',)
        labels = {'purchase_place':'購入場所'}
    
    def clean_purchase_place(self):
        purchase_place = self.cleaned_data['purchase_place']
        if purchase_place:
            purchase_place_number = PurchasePlace.objects.filter(purchase_place=purchase_place).count()
            if purchase_place_number > settings.PURCHASE_PLACE_MAX:
                self.add_error('purchase_place',f"購入場所に設定出来る件数は{settings.PURCHASE_PLACE_MAX}件までです。")
        return purchase_place


class ClosetCreateForm(forms.ModelForm):

    class Meta:
        model = Closet
        fields = ('closet_name',)
        labels = {'closet_name':'クローゼット名'}
    
    def clean_closet_name(self):
        closet_name = self.cleaned_data['closet_name']
        if closet_name:
            closet_name_number = Closet.objects.filter(closet_name=closet_name).count()
            if closet_name_number > settings.CLOSET_NAME_MAX:
                self.add_error('closet_name',f"開設できるクローゼットは{settings.CLOSET_NAME_MAX}です。")
        return closet_name


class ItemCreateForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('item_name','purchase_date', 'pricing', 'season','occasion', 'item_image','favorite_level', 'item_importance','closet', 'item_type','item_color','item_brand',
        'purchase_place', 'memo',)

        labels = {'item_name':'アイテム名称','item_type':'アイテム種類','season':'季節','occasion':'シーン','pricing':'購入価格(円)','purchase_date':'購入日','closet':'クローゼット',
        'item_color':'アイテムカラー','item_brand':'ブランド','purchase_place':'購入場所','item_image':'アイテム画像','favorite_level':'お気に入り度','item_importance':'大事さ','memo':'メモ',}

        widgets = {
            'season': forms.RadioSelect(choices=SEASON_CHOICES),
            'occasion': forms.RadioSelect(choices=OCCASION_CHOICES),
            'purchase_date': forms.SelectDateWidget(years = [x for x in range(2000,2040)], months = MONTHS),
        }

