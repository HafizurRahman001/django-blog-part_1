from django.shortcuts import render,redirect
from profile_app.forms import ProfileForm

# Create your views here.
def add_profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            print(profile_form.cleaned_data)
            profile_form.save()
            return redirect('add_profile')
    else:
        profile_form = ProfileForm()
    return render(request,'add_profile.html', {'form':profile_form})
