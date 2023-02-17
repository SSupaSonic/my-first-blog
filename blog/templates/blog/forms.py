from django import forms
#from blog.models import Image
from blog.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ('title', 'image')