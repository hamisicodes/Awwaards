from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from .forms import UserRegistrationForm,UserEditForm,ProfileEditForm,
from .models  import  Profile
from  django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit= False)
            # set the chose password
            new_user.set_password(user_form.cleaned_data['password'])
            # save the new user
            new_user.save()
            Profile.objects.create(user= new_user)
            messages.success(request ,'Account created successfully')
            return redirect('dashboard')

        else:
            messages.error(request ,'Error creating your account')
            return render(request,'account/register.html' , {'user_form':user_form})


    else:
        user_form = UserRegistrationForm()

        return render(request,'account/register.html' , {'user_form':user_form})

def dashboard(request):
    return render(request,'base.html')

@login_required
def edit(request):
    if request.method == 'POST':
        user_form =UserEditForm(instance=request.user , data=request.POST)
        profile_form =ProfileEditForm(instance = request.user.profile, data =request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request ,'Profie updated successfully')
        
        else:
            messages.error(request,'Error updating profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form':user_form , 'profile_form':profile_form})
