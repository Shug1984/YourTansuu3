from django import forms
from django.conf import settings

from .models import ItemType, ItemColor, ItemBrand, PurchasePlace, Closet, Item, FAVORITE_LEVEL_CHOICES, ITEM_IMPORTANCE_CHOICES, SEASON_CHOICES, OCCASION_CHOICES

MONTHS = {
    1: '1月', 2: '2月', 3: '3月', 4: '4月',
    5: '5月', 6: '6月', 7: '7月', 8: '8月',
    9: '9月', 10: '10月', 11: '11月', 12: '12月'
}

class ClosetForm(forms.ModelForm):

    class Meta:
        model = Closet
        fields = ('closet_name', 'closet_memo')
        labels = {'closet_name':'クローゼット名', 'closet_memo':'クローゼットメモ'}


class ItemForm(forms.ModelForm):
    item_type = forms.ModelChoiceField(queryset=ItemType.objects.all(), label='アイテム種類', empty_label='選択してください', widget=forms.TextInput)

    class Meta:
        model = Item

        fields = ('item_type', 'item_name', 'purchase_date', 'pricing', 'item_image',
        'memo')

        labels = {'item_type':'アイテム種類', 'item_name':'アイテム名称', 'purchase_date':'購入日', 'pricing':'購入価格(円)', 'item_image':'アイテム画像', 
        'memo':'メモ'}

        widget = {
            'season': forms.RadioSelect(choices=SEASON_CHOICES),
            'occasion': forms.RadioSelect(choices=OCCASION_CHOICES),
            'purchase_date': forms.SelectDateWidget(years = [x for x in range(2000,2040)], months = MONTHS),
            'favorite_level': forms.RadioSelect(choices = FAVORITE_LEVEL_CHOICES ),
            'item_importance': forms.RadioSelect(choices = ITEM_IMPORTANCE_CHOICES),
        }


"""
 item_type = forms.ModelChoiceField(queryset=ItemType.objects.all(), label='アイテム種類', empty_label='選択してください', widget=forms.TextInput)
 item_color = forms.ModelChoiceField(queryset=ItemColor.objects.all(), label='アイテムカラー', empty_label='選択してください', initial='', widget=forms.TextInput)
 item_brand = forms.ModelChoiceField(queryset=ItemBrand.objects.all(), label='ブランド', empty_label='選択してください', initial='', widget=forms.TextInput)
 purchase_place = forms.ModelChoiceField(queryset=PurchasePlace.objects.all(), label='購入場所', empty_label='選択してください', initial='', widget=forms.TextInput)




"""
    