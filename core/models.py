from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
import uuid


AGE_CHOICES = (
    ('All' , 'All'),
    ('Kids' , 'Kids')
)

MOVIE_TYPE=(
    ('single','Single'),
    ('seasonal','Seasonal')
)

class CustomUser(AbstractUser):
    profile = models.ManyToManyField("Profile", verbose_name=_("profile") , blank=True , null=True)


    class Meta:
        verbose_name = _("CustomUser")
        verbose_name_plural = _("CustomUsers")

 



class Profile(models.Model):
    """Model definition for Profile."""
    name = models.CharField(_("name"), max_length=50)
    age_limit = models.CharField(_("age limit"), choices=AGE_CHOICES,max_length=10)
    uuid = models.UUIDField(_("uuid") , default=uuid.uuid4)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return self.name


class Movie(models.Model):
    title:str=models.CharField(max_length=225)
    description:str=models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    type=models.CharField(max_length=10,choices=MOVIE_TYPE)
    videos=models.ManyToManyField('Video')
    flyer=models.ImageField(upload_to='flyers',blank=True,null=True)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES,blank=True,null=True)

class Video(models.Model):
    title:str = models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')
    



