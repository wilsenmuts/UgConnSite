from django.forms import ModelForm
#from .models import users
from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

'''
Mapping to the user model
'''


class UgBuSForm(forms.Form):
    title = forms.CharField(label='Title', max_length=35)
    options = forms.CharField(label='About ', max_length=35)
    message = forms.CharField(widget=forms.Textarea)
'''
class UserLoginForm(forms.Form):
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data('username')
        password = self.changed_data('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(label='Password'))
    password2 = forms.CharField(widget=forms.PasswordInput(label='Password'))

    class Meta:
        model = User
        fields = [
            'username',
            'firstname'
            'surname',
            'email',
            'password',
            'password2'
        ]

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password = self.cleaned_data.get.get('password2')
        if password != password2:
            raise forms.ValidationError('passwords do not match')
'''