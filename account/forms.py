import datetime
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, PasswordChangeForm, PasswordResetForm, SetPasswordForm

from .models import MyUser

class UserCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = datetime.date.today()
        year = today.year
        years = [x for x in range(year-100, year)]
        self.fields['date_of_birth'].widget = forms.SelectDateWidget(years=years)
    
    password1 = forms.CharField(label='パスワード', widget=forms.PasswordInput(render_value=True))
    password2 = forms.CharField(label='パスワード確認', widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = MyUser

        fields = ('email','password1','password2','last_name','first_name','last_kana','first_kana','zip_code','prefecture','city_name',
        'street_name','building_name', 'tel', 'date_of_birth', 'gender', 'personal_image')

        labels = {'email':'メールアドレス','password1':'パスワード','password2':'パスワード確認','last_name':'姓','first_name':'名','last_kana':'姓(カナ)','first_kana':'名(カナ)',
        'zip_code':'郵便番号','prefecture':'都道府県','city_name':'市町村','street_name':'丁目・番地','building_name':'建物名', 'tel':'電話番号', 'date_of_birth':'生年月日', 
        'gender':'性別', 'personal_image':'画像'}
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("パスワードが一致しません")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        
        fields = ('last_name','first_name','last_kana','first_kana','zip_code','prefecture','city_name',
        'street_name','building_name', 'tel', 'date_of_birth', 'gender', 'personal_image')

        labels = {'last_name':'姓','first_name':'名','last_kana':'姓(カナ)','first_kana':'名(カナ)',
        'zip_code':'郵便番号','prefecture':'都道府県','city_name':'市町村','street_name':'丁目・番地','building_name':'建物名', 'tel':'電話番号', 'date_of_birth':'生年月日', 
        'gender':'性別', 'personal_image':'画像'}

    #def clean_password(self):
    #    return self.initial["password"]


class UserForm(forms.ModelForm):
    form = UserChangeForm
    add_form = UserCreationForm

    class Meta:
        model = MyUser

        fields = (
            'email','password','last_name','first_name','last_kana','first_kana','zip_code','prefecture','city_name','street_name','building_name','tel','gender','personal_image'
        )
        
        labels = {
            'email':'メールアドレス','password':'パスワード','last_name':'姓','first_name':'名','last_kana':'姓(カナ)','first_kana':'名(カナ)','zip_code':'郵便番号',
            'prefecture':'都道府県','city_name':'市町村','street_name':'丁目・番地','building_name':'建物名','tel':'電話番号','gender':'性別','personal_image':'画像'
        }

        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='メールアドレス', max_length=155)
    password = forms.CharField(label='パスワード', max_length=155, widget=forms.PasswordInput())


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class MyPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.value():
            field.widget.attrs['class'] = 'form-control'


class MySetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


        

