from django import forms
from creationgroups.Media import Group

                                    
class AddGroupForm(forms.Form):
    def __init__(self, user, thedisk, *args, **kwargs):
        super(AddGroupForm, self).__init__(*args,**kwargs)
        self.user = user
        self.disk = thedisk
        
    name = forms.CharField(max_length=250)
    description= forms.CharField(widget=forms.Textarea())
    
    def save(self):
        return Group.objects.create(name=self.cleaned_data['name'],
                                    description = self.cleaned_data['description'],
                                    user = self.user,
                                    disk = self.disk)
    