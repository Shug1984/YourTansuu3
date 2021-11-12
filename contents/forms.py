from django import forms
from django.conf import settings

from .models import (Item, Closet, ItemType, ItemColor, ItemBrand, PurchasePlace, SEASON_CHOICES, OCCASION_CHOICES, ITEM_IMPORTANCE_CHOICES, FAVORITE_LEVEL_CHOICES)

MONTHS = {
    1: '1月', 2: '2月', 3: '3月', 4: '4月',
    5: '5月', 6: '6月', 7: '7月', 8: '8月',
    9: '9月', 10: '10月', 11: '11月', 12: '12月'
}


class ClosetCreateForm(forms.ModelForm):

    class Meta:
        model = Closet
        fields = ('closet_name',)
        labels = {'closet_name':'クローゼット名'}


class ItemTypeCreateForm(forms.ModelForm):

    class Meta:
        model = ItemType
        fields = ('item_type',)
        labels = {'item_type':'アイテム種類'}


class ItemColorCreateForm(forms.ModelForm):

    class Meta:
        model = ItemColor
        fields = ('item_color',)
        labels = {'item_color':'アイテムカラー'}


class ItemBrandCreateForm(forms.ModelForm):

    class Meta:
        model = ItemBrand
        fields = ('item_brand',)
        labels = {'item_brand':'ブランド名'}


class PurchasePlaceCreateForm(forms.ModelForm):

    class Meta:
        model = PurchasePlace
        fields = ('purchase_place',)
        labels = {'purchase_place':'購入場所'}


class ItemCreateForm(forms.ModelForm):
    item_type= forms.ModelChoiceField(queryset=ItemType.objects.all(), empty_label='工事中', widget=forms.TextInput)
    item_color= forms.ModelChoiceField(queryset=ItemColor.objects.all(), empty_label='工事中')
    item_brand= forms.ModelChoiceField(queryset=ItemBrand.objects.all(), empty_label='工事中')
    purchase_place= forms.ModelChoiceField(queryset=PurchasePlace.objects.all(), empty_label='工事中')
    
    class Meta:
        model = Item
        fields = ('item_name','item_type','item_color','item_brand','purchase_place', 'closet_name', 'season','occasion','pricing','purchase_date','item_image','favorite_level',
        'item_importance', 'memo',)

        labels = {'item_name':'アイテム名称','item_type':'アイテム種類','season':'季節','occasion':'シーン','pricing':'購入価格(円)','purchase_date':'購入日','closet_name':'クローゼット',
        'item_color':'アイテムカラー','item_brand':'ブランド','purchase_place':'購入場所','item_image':'アイテム画像','favorite_level':'お気に入り度','item_importance':'大事さ','memo':'メモ',}

        widgets = {
            'season': forms.RadioSelect(choices=SEASON_CHOICES),
            'occasion': forms.RadioSelect(choices=OCCASION_CHOICES),
            'purchase_date': forms.SelectDateWidget(years = [x for x in range(2000,2040)], months = MONTHS),
            'favorite_level': forms.RadioSelect(choices = FAVORITE_LEVEL_CHOICES ),
            'item_importance': forms.RadioSelect(choices = ITEM_IMPORTANCE_CHOICES),
        }
