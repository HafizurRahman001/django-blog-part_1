from django.shortcuts import render
from posts_app.models import Post

# Create your views here.
def home(request):
    post_data = Post.objects.all()
    return render(request,'displayData.html', {'postData':post_data})