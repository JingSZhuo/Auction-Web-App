from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    custom_user_email = models.EmailField(max_length=254, unique=True, default=True)
    #custom_username = models.CharField(max_length=255, default=True)

    #USERNAME_FIELD = 'custom_user_email'


class User(models.Model):
    user_email = models.EmailField(max_length=254)
    user_dob = models.DateField()

    # to use ImageField you will need to install Pillow
    #pip install Pillow
    
    user_profilePicture = models.ImageField()

    def __str__(self):
        return self.user_email
    def __str__(self) -> str:
        return str(self.user_dob)


    def to_dict(self):
        return{
            'id': self.id,
            'user_email': self.user_email,
            'user_dob': self.user_dob,
            'user_profilePicture': self.user_profilePicture
        }

class Item(models.Model):
    item_title=models.CharField(max_length=254)
    item_description=models.CharField(max_length=2000)
    item_sprice=models.DecimalField(max_digits=100,decimal_places=2)
    item_picture=models.CharField(max_length=254)
    item_auctionfinish=models.DateTimeField()

    def __str__(self):
        return self.item_title

    def __str__(self):
        return self.item_description

    def __str__(self):
         return str(self.item_sprice)

    def __str__(self) -> str:
        return self.item_picture

    def __str__(self) -> str:
        return str(self.item_auctionfinish)


    def to_dict(self):
        return{
            'id': self.id,
            'item_title': self.item_title,
            'item_description': self.item_description,
            'item_sprice': self.item_sprice,
            'item_picture': self.item_picture,
            'item_auctionfinish': self.item_auctionfinish
        }
