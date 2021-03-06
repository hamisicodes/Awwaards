from django import forms
from.models import Profile,Project,Rate
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label ='Password',
                                widget = forms.PasswordInput)

    password2 =forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ('username','first_name' , 'email')    
    
    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords dont match')
    
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth','photo','bio')

class ProjectForm(forms.ModelForm):
    class Meta:
        model =Project
        fields = ('title','description','image','link')

class RateForm(forms.ModelForm):
    class Meta:
        model= Rate
        fields = ('usability','design','content')
