import datetime
from django.db import models
from django.conf import settings


SEASON_CHOICES = [('spring','春'),('summer','夏'),('fall','秋'),('winter','冬')]
OCCASION_CHOICES = [('daily_use','普段着'),('work_wear','仕事'),('active_wear','よそ行き'),('sports_wear','スポーツ'),('other_use','その他')]
FAVORITE_LEVEL_CHOICES = [(1,'めちゃ低い'),(2,'低い'),(3,'普通'),(4,'高い'),(5,'めちゃ高い')]
ITEM_IMPORTANCE_CHOICES = [(1,'捨てれる'),(2,'悩む'),(3,'普通'),(4,'まあ大事'),(5,'めっちゃ大事')]


class Closet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    closet_name = models.CharField(verbose_name='クローゼット名', max_length=255)

    class Meta:
        ordering =['closet_name']
    
    def __str__(self):
        return self.closet_name

class ItemType(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    item_type = models.CharField(verbose_name='アイテム種類', max_length=255)

    def __str__(self):
        return self.item_type

class ItemColor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    item_color = models.CharField(verbose_name='アイテムカラー', max_length=255)

    def __str__(self):
        return self.item_color

class ItemBrand(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    item_brand = models.CharField(verbose_name='ブランド', max_length=255)

    def __str__(self):
        return self.item_brand

class PurchasePlace(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    purchase_place = models.CharField(verbose_name='購入場所', max_length=255)

    def __str__(self):
        return self.purchase_place


class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.CASCADE,null=True)
    item_type = models.ForeignKey(ItemType, verbose_name='アイテム種類', max_length=255, default=None, on_delete=models.PROTECT)
    item_color = models.ForeignKey(ItemColor, verbose_name='アイテム色', max_length=20, default=None, on_delete=models.PROTECT)
    item_brand = models.ForeignKey(ItemBrand, verbose_name='ブランド', max_length=150, default=None, on_delete=models.PROTECT)
    purchase_place = models.ForeignKey(PurchasePlace, verbose_name = '購入場所', max_length=255, default=None, on_delete=models.PROTECT)
    closet_name = models.ForeignKey(Closet, verbose_name = 'クローゼット名', max_length=255, default=None, on_delete=models.PROTECT)
    season = models.CharField(verbose_name = '季節', max_length=10, choices = SEASON_CHOICES, default='spring')
    occasion = models.CharField(verbose_name = 'シーン', max_length=30, choices = OCCASION_CHOICES, default='daily_use')
    item_name = models.CharField(verbose_name = 'アイテム名称', max_length=300)
    purchase_date = models.DateTimeField(verbose_name = '購入日', blank=True, null=True)
    pricing = models.IntegerField(verbose_name = '購入価格(円)', )
    item_image = models.ImageField(verbose_name = 'アイテム画像', upload_to='contens/item_images', blank = True, null=True)
    memo = models.TextField(verbose_name = 'メモ', blank=True, null=True)
    favorite_level = models.IntegerField(verbose_name = 'お気に入り度', choices = FAVORITE_LEVEL_CHOICES, default=None, blank=True, null=True)
    item_importance = models.IntegerField(verbose_name = '大事さ', choices = ITEM_IMPORTANCE_CHOICES, default=None, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name = '作成日', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name = '更新日', auto_now=True)
    

    class Meta:
        ordering = ['item_name']
    
    def __str__(self):
        return self.item_name


# Create your models here.
