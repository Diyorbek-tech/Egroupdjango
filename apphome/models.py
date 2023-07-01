from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=60,help_text="Bu yerga userning ismini kiritasiz!")
    surname=models.CharField(max_length=60,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    age=models.IntegerField(default=20)
    biography=models.TextField(null=True,blank=True)


    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class Images(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)

      image=models.ImageField(upload_to=f"images/")

      def __str__(self):
          return self.user.name