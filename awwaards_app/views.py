from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistratinForm(request.POST)
        
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
        user_form = UserRegistratinForm()

        return render(request,'account/register.html' , {'user_form':user_form})
