from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from .forms import UserRegistrationForm,UserEditForm,ProfileEditForm,ProjectForm,RateForm
from .models  import  Profile,Project,Rate
from  django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
    projects = Project.objects.all()


    return render(request,'account/dashboard.html',{'projects':projects})

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

def profile(request):
    profile = Profile.objects.get(user__id = request.user.id)

    return render(request ,'account/profile.html' , {'profile':profile})


def get_profile(request,username):
  
    profile = Profile.objects.get(user__username = username) 

    return render(request ,'account/profile.html' , {'profile':profile})


@login_required
def create(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST,request.FILES)
        profile = Profile.objects.get(user__id = request.user.id)

        if project_form.is_valid():
            post = project_form.save(commit = False)
            post.author = profile
            post.save()

            messages.success(request ,'New Project added successfully')
            return redirect('dashboard')

    else:
        project_form = ProjectForm()
        return render(request,'account/project.html', {'project_form':project_form})

def rate(request,pk):
    project = Project.objects.get(pk = pk)
    if request.method == 'POST':
        rate_form = RateForm(request.POST)
        if rate_form.is_valid():
            rate = rate_form.save(commit = False)
            rate.user= request.user
            rate.project = project
            rate.save()
    else:
        rate_form = RateForm()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def single(request,pk):
    project = Project.objects.get(pk = pk)
    rate_form = RateForm()
    return render(request,'account/single.html', {'rate_form':rate_form, 'project':project})


def searches(request):
    if request.GET.get('search'):
        search = request.GET['search']
        projects = Project.search_projects(search)
        searchterm = f'{search}'
        return render(request,'account/search.html' , {'projects':projects, 'searchterm':searchterm})
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



        






