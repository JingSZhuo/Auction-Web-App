from django.db import models

# Create your models here.
class User(models.Model):
    user_email = models.EmailField(max_length=254)
    user_dob = models.DateField()

    # to use ImageField you will need to install Pillow
    #pip install Pillow
    
    user_profilePicture = models.ImageField()

    def __str__(self):
        return self.user_email
    def __str__(self):
        return self.user_dob


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
    item_picture=models.ImageField()
    item_auctionfinish=models.DateTimeField()

    def __str__(self):
        return self.item_title

    def __str__(self):
        return self.item_description

    def __str__(self):
        return self.item_sprice

    def __str__(self):
        return self.item_auctionfinish

    def to_dict(self):
        return{
            'id': self.id,
            'item_title': self.item_title,
            'item_description': self.item_description,
            'item_sprice': self.item_sprice,
            'item_picture': self.item_picture,
            'item_auctionfinish': self.item_auctionfinish
        }
