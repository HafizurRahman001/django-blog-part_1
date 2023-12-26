from django.shortcuts import render,redirect
from posts_app.forms import AddPostForm
from posts_app.models import Post

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        add_post_form = AddPostForm(request.POST)
        if add_post_form.is_valid():
            add_post_form.save()
            return redirect('add_post')
    else:
        add_post_form = AddPostForm()
    return render(request,'add_post.html', {'form':add_post_form})


def edit_post(request,id):
    post = Post.objects.get(pk=id)
    add_post_form = AddPostForm(instance=post)
    if request.method == 'POST':
        add_post_form = AddPostForm(request.POST, instance=post)
        if add_post_form.is_valid():
            add_post_form.save()
            return redirect('home')
    return render(request,'add_post.html', {'form':add_post_form})


def delete_post(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')

