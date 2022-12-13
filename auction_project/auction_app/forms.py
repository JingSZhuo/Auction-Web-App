from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from auction_app.models import CustomUser


class CustomUserSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')
        
        

class CustomUserChangeForm(UserChangeForm):
    
    class Meta: 
        model = CustomUser
        fields = ('email',)

