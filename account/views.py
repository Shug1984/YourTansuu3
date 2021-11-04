from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponse

from .forms import UserForm, UserCreationForm, UserChangeForm, MyPasswordChangeForm, UserLoginForm
from .models import MyUser
from .utils import decode_base64_file

def topview(request):
    return render(request, 'account/top.html')


@login_required
def homeview(request):
    return render(request, 'account/home.html')


def signupview(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            action = request.POST['action']
            if action == 'input':
                return render(request, 'account/signup.html',{'form':form})
            elif action == 'confirm':
                return render(request, 'account/signup_confirm.html',{'form':form, 'personal_image_base64': request.POST.get('personal_image_base64'),})
            else:
                form = form.save(commit=False)
                form.personal_image = decode_base64_file(request.POST.get('personal_image'), request.POST.get('personal_image_base64'))
                form.save()
                return redirect('signup_complete')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html',{'form':form})


def signup_completeview(request):
    return render(request, 'account/signup_complete.html')


def loginview(request):
    if request.method == 'POST':
        email_data = request.POST['email_data']
        password_data = request.POST['password_data']
        user = authenticate(request, email=email_data, password=password_data)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'account/login.html',{'error_message':'ログイン出来ません'})
   

@login_required
def logoutview(request):
    logout(request)
    return render(request, 'account/logout.html')


@login_required
def user_informationview(request, pk):
    user_id = request.user.pk
    user_information = MyUser.objects.get(pk=user_id)
    context = {'user_information':user_information}
    return render(request, 'account/user_information.html', context)


@login_required
def user_updateview(request, pk):
    user_id = request.user.pk
    user_information = MyUser.objects.get(pk=user_id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, request.FILES, instance=user_information)
        if form.is_valid():
            form.save()
            return redirect('user_information', pk=pk)
    else:
        form = UserChangeForm(instance=user_information)
    return render(request, 'account/user_update.html', {'form':form, 'user_information':user_information})


class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('password_change_complete')


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'account/password_change_complete.html'


class PasswordResetView(PasswordResetView):
    pass


class PasswordResetDone(PasswordResetDoneView):
    pass


class PasswordResetConfirm(PasswordResetConfirmView):
    pass
    

class PasswordResetComplete(PasswordResetCompleteView):
    pass
    





# Create your views here.
