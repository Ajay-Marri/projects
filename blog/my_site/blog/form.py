from django import forms
from .models import Comment

class commetform(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=["post"]
        labels={
            "user_name":"Name",
            "user_email":"E-mail",
            "text":"Comment"
        }