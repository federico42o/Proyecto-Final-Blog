from django import forms
from .models import Post, Comment

class PostForm (forms.ModelForm):
    class Meta : 
        model=Post
        fields= ["title",'image', "content", "description","author",'category']

class CommentPost(forms.ModelForm):
    class Meta : 
        model=Comment
        fields= ["posts","content","author"]
