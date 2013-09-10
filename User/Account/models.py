from django.db import models
from django.contrib.auth.models import User
from django import forms

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=30,
                                widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(max_length=30,
                                widget=forms.PasswordInput(render_value=False))
    '''
    we add widget because HTML has an <input type="password"> in its handling
    thus the password widget will render itself as that <input type="password">
    render value tells it that if it has some data it shouldnt show it(so if 
    user types wrong the first time it clears the field for second time).
    to declare a field optional pass in required=False
    '''

                                
    #custom validation (takes name clean_ and particular form)
    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("This usename is already in use.\
        Please choose another.")
    #cleaned_data is any data that has made it through validation so far (dict)
    
    
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("You must type the same password each\
                time")
        return self.cleaned_data
    #first checks if passwords are in cleaned data, then checks if equal
    #clean applies form as a whole. whereas clean_password is only password
    
        
    def save(self):
        new_user = User.objects.create_user(username=self.cleaned_data['username'],
                                            email=self.cleaned_data['email'],
                                            password=self.cleaned_data['password1'],
                                            first_name=self.cleaned_data['first_name'],
                                            last_name=self.cleaned_data['last_name'])
        return new_user


class Disk(models.Model):
    letter = models.CharField(max_length=3)
    name = models.CharField(max_length=30, blank=True)
    space_allocated = models.BigIntegerField(default=5368709120)
    space_used = models.BigIntegerField()
    space_left = models.BigIntegerField()
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return '%s:%s' %(self.letter, self.name)