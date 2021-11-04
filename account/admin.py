from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import MyUser


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email','last_name','first_name','last_kana','first_kana','zip_code','prefecture','city_name',
        'street_name','building_name', 'tel', 'date_of_birth', 'gender', 'personal_image', 'is_active', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1','password2','last_name','first_name','last_kana','first_kana','zip_code','prefecture','city_name',
        'street_name','building_name', 'tel', 'date_of_birth', 'gender', 'personal_image', 'is_active', 'is_admin')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)



# Register your models here.
