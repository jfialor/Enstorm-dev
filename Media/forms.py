import os
import errno
from django import forms
from models import *
from User.Creations.creationgroups.Media import Group


                                    
class AddMediaForm(forms.Form):
        
    name = forms.CharField(max_length=250)
    
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes', 
        required = False
    )
    
    
    description_body = forms.CharField(widget=forms.Textarea(), required=False)
    description_excerpt = forms.CharField(widget=forms.Textarea(), required=False)
    category = forms.ModelChoiceField(queryset=Type.objects.all(), required=False)
    orig_shelf = forms.ModelChoiceField(queryset=Group.objects.all(),required=False)
    enable_comments = forms.BooleanField(required=False)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)
    public = forms.BooleanField(required=False)
    
    
    #Unnecessary now.
    def handle_uploaded_file(self, path_directory, file):
        self.make_sure_path_exists(path_directory)
        path_directory += file.name
        
        with open(path_directory, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return path_directory
                
    def make_sure_path_exists(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        
            '''
        try:
            os.makedirs(path)
        except OSError as exception:
            pass
            #if exception.errno != errno.EEXIST:  - knowing what the error is
                #raise
                '''
    
    """
    def save(self):
        return Book.objects.create(name=self.cleaned_data['name'],
                                    #path to docfile=path,
                                    description_full = self.cleaned_data['description_full'],
                                    description_excerpt = self.cleaned_data['description_excerpt'],
                                    artist = self.artist,
                                    category = self.cleaned_data['category'],
                                    orig_shelf = self.cleaned_data['orig_shelf'],
                                    enable_comments = self.cleaned_data['category'],
                                    status = self.cleaned_data['status'])
    """
    
        