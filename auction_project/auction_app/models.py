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
    def __str__(self):
        return self.user_profilePicture


    def to_dict(self):
        return{
            'id': self.id,
            'user_email': self.user_email,
            'user_dob': self.user_dob,
            'user_profilePicture': self.user_profilePicture
        }