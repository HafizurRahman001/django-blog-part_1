from django import forms
from posts_app.models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        