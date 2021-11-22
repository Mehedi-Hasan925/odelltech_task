from django import forms
from app_user_info import models

class user_info_form(forms.ModelForm):
    # name = forms.CharField(required=True, label="",widget=forms.TextInput(attrs={'placeholder':'Full Name','class':'mb-2'}))
    # country = forms.ForeignKeyField(required=True, label="",widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'mb-2'}))
    # email = forms.EmailField(required=True, label="",widget=forms.TextInput(attrs={'placeholder':'Email','class':'mb-2'}))
    # username = forms.CharField(required=True, label="",widget=forms.TextInput(attrs={'placeholder':'Username','class':'mb-2'}))
    # password1 = forms.CharField(required=True, label="",widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'mb-2'}))
    # password2 = forms.CharField(required=True, label="",widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'mb-2'}))
    class Meta:
        model = models.User_info
        fields = ('name','country','Division','District','upazilla')
        