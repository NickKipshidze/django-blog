from django import forms
from . import models
 
class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model = models.BlogPost
        fields = ["title", "thumbnail"]
