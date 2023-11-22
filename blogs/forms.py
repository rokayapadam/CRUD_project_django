from django import forms
from .models import User

class BlogsFOrm(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['id', 'name', 'email', 'password']
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'})
        }
       