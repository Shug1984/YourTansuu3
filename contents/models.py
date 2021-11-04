import datetime
from django.db import models
from django.conf import settings

ITEM_TYPE_CHOICES = [('jacket','上着'),('shirt','シャツ'),('pants','パンツ'),('underpants','下着(下)'),('undershirt','下着(上)'),('socks','靴下'),('others','その他')]
ITEM_COLOR_CHOICES = [('red','赤'),('blue','青'),('green','緑'),('yellow','黄'),('purple','紫'),('orange','橙'),('black','黒'),('white','白'),('grey','灰'),('beige','ベージュ'),('navy','ネイビー'),('brown','茶'),('others','その他')]
SEASON_CHOICES = [('spring','春'),('summer','夏'),('fall','秋'),('winter','冬')]
OCCASION_CHOICES = [('daily_use','普段着'),('work_wear','仕事'),('active_wear','よそ行き'),('sports_wear','スポーツ'),('other_use','その他')]
FAVORITE_LEVEL_CHOICES = [(1,'めちゃ低い'),(2,'低い'),(3,'普通'),(4,'高い'),(5,'めちゃ高い')]
ITEM_IMPORTANCE_CHOICES = [(1,'捨てれる'),(2,'悩む'),(3,'普通'),(4,'まあ大事'),(5,'めっちゃ大事')]


class ItemType(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    item_type = models.CharField(verbose_name='アイテム種類', max_length=155)


class ItemColor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    item_color = models.CharField(verbose_name='アイテムカラー', max_length=100)


class ItemBrand(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    item_brand = models.CharField(verbose_name='ブランド', max_length=155)


class PurchasePlace(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    purchase_place = models.CharField(verbose_name='購入場所', max_length=155)
    

class Closet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE, null=True)
    closet_name = models.CharField(verbose_name='クローゼット名', max_length=255)
    closet_memo = models.CharField(verbose_name='クローゼットメモ', max_length=325)
    create_date = models.DateTimeField(verbose_name='クローゼット作成日', auto_now_add=True)

    class Meta:
        ordering =['create_date']
    
    def __str_(self):
        return self.closet_name


class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE, null=True)
    item_type = models.CharField(verbose_name='アイテム種類', null=True, blank=True, default='', max_length=155)
    item_color = models.ForeignKey(ItemColor, verbose_name='アイテムカラー', blank=True, null=True, default='', on_delete=models.PROTECT)
    item_brand = models.ForeignKey(ItemBrand, verbose_name='ブランド名称', blank=True, null=True, default='', on_delete=models.PROTECT)
    purchase_place = models.ForeignKey(PurchasePlace, verbose_name='購入場所', blank=True, null=True,  default='', on_delete=models.PROTECT)
    item_name = models.CharField(verbose_name='アイテム名称', max_length=300)
    purchase_date = models.DateTimeField(verbose_name='購入日', blank=True, null=True)
    pricing = models.IntegerField(verbose_name='購入価格(円)',)
    item_image = models.ImageField(verbose_name='アイテム画像', upload_to='', blank=True, null=True)
    memo = models.TextField(verbose_name='メモ', blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='アイテム登録日', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='アイテム更新日', auto_now=True)
    closet = models.ForeignKey(Closet, on_delete=models.PROTECT, blank=True, null=True, default=None)
    season = models.CharField(verbose_name = '季節', max_length=10, choices = SEASON_CHOICES, default='spring')
    occasion = models.CharField(verbose_name = 'シーン', max_length=30, choices = OCCASION_CHOICES, default='daily_use')
    favorite_level = models.IntegerField(verbose_name = 'お気に入り度', choices = FAVORITE_LEVEL_CHOICES, blank=True, null=True, default='1')
    item_importance = models.IntegerField(verbose_name = '大事さ', choices = ITEM_IMPORTANCE_CHOICES, blank=True, null=True, default='1')

    class Meta:
        ordering = ['item_name']

    def __str__(self):
        return self.item_name

