from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, date_of_birth, profile_picture, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('Invalid Email')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            date_of_birth=date_of_birth,
            profilePicture=profile_picture,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=None,
            profile_picture=None,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        user.save(using=self._db)             #save to local sqlite database
        return user
    
"""Custom User Model | Profile Model"""    

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True, default="")
    date_of_birth = models.DateField(null=True, blank=True)
    profilePicture = models.CharField(max_length=254, default="")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    object = CustomUserManager()
    
    def __str__(self) -> str:
        return str(self.date_of_birth)
    
    def __str__(self) -> str:
        return str(self.profilePicture)
    
    def __str__(self) -> str:
        return self.email
    
    def to_dict(self):
        return{
            'id': self.id,
            'user_email': self.email,
            'user_dob': self.date_of_birth,
            'user_profilePicture': self.profilePicture
        }



# class User(models.Model):
#     user_email = models.EmailField(max_length=254)
#     user_dob = models.DateField()

#     # to use ImageField you will need to install Pillow
#     #pip install Pillow
    
#     user_profilePicture = models.ImageField()

#     def __str__(self) -> str:
#         return self.user_email
#     def __str__(self) -> str:
#         return str(self.user_dob)


#     def to_dict(self):
#         return{
#             'id': self.id,
#             'user_email': self.user_email,
#             'user_dob': self.user_dob,
#             'user_profilePicture': self.user_profilePicture
#         }

class Item(models.Model):
    item_title=models.CharField(max_length=254)
    item_description=models.CharField(max_length=2000)
    item_sprice=models.DecimalField(max_digits=100,decimal_places=2)
    item_picture=models.CharField(max_length=254)
    item_auctionfinish=models.DateTimeField(null=True, blank=True)
    item_personHighestBid=models.EmailField(max_length=254, default="tbd")
    item_image=models.ImageField(upload_to='./auction_app_vue_frontend/src/Images', height_field=50, width_field=50, max_length=100, null=True, default=None)


    def __str__(self):
        return self.item_description

    def __str__(self):
         return str(self.item_sprice)

    def __str__(self) -> str:
        return self.item_picture

    def __str__(self) -> str:
        return str(self.item_auctionfinish)

    def __str__(self) -> str:
        return self.item_personHighestBid
    
    def __str__(self):
        return self.item_title


    def to_dict(self):
        return{
            'id': self.id,
            'item_title': self.item_title,
            'item_description': self.item_description,
            'item_sprice': self.item_sprice,
            'item_picture': self.item_picture,
            'item_auctionfinish': self.item_auctionfinish,
            'item_personHighestBid':self.item_personHighestBid
        }
