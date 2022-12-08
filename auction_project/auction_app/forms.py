from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from auction_app.models import CustomUser


class CusomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)
        
        

class CustomUserChangeForm(UserChangeForm):
    
    class Meta: 
        model = CustomUser
        fields = ('email',)

