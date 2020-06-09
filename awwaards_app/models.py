from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Create your models here.
class  Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) #To refer the user model
    date_of_birth = models.DateField(blank =True, null =True)
    photo = models.ImageField(upload_to='users/' ,  default='../static/photos/profile.jpeg')
    bio = models.TextField(default="Hello awwaards, Its nice being here")

    def save_profile(self):
        self.save()
        

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username

    @classmethod
    def search_profile(cls,name):
        profile = cls.objects.filter(user__username__icontains = name)
        return profile

    @classmethod
    def get_profile(cls,id):
        profile = cls.objects.get(id = id)
        return profile


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    publish_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField()

    def save_project(self):
        self.save()
        

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.title

    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    class Meta:
        ordering = ['-publish_at']

class Rate(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE, null=True)
    design = models.PositiveIntegerField(default = 0 , validators =[ MaxValueValidator(10)] )
    design = models.PositiveIntegerField(default = 0 , validators =[ MaxValueValidator(10)] )
    design = models.PositiveIntegerField(default = 0 , validators =[ MaxValueValidator(10)] )