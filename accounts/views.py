from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .forms import SignUp, UserEdit, ProfileEdit
from .models import Profile
from music.models import Song
# Create your views here.

def home_page(request):
	if request.user.is_authenticated:
		return redirect('music:index')
	return render(request,'accounts/index.html',{})

def signUp(request):
    if request.method == 'POST':
        form = SignUp(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password2'])
            new_user.save()
            profile=Profile.objects.create(user=new_user)
            profile.profile_pic = form.cleaned_data.get('profile_pic')
            profile.save()
            return redirect('accounts:login')
    else:
        form = SignUp()
    return render(request, 'accounts/register.html',{'form': form}) 

def login_view(request):
	if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
	        login(request, user)
	        return redirect('music:index')
	    else:
	    	messages.error(request, "Invalid username or password")
	form = AuthenticationForm()
	return render(request,'accounts/login.html', {'form' : form})

def logout_view(request):
	logout(request)
	return render(request, 'accounts/logged_out.html',{})


@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile,pk=request.user.profile.id)
    user = profile.user
    if request.method == 'POST':
        user_form = UserEdit(request.POST,instance=request.user)
        profile_form = ProfileEdit(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('dashboard')
    else:
        user_form = UserEdit(instance=user)
        profile_form = ProfileEdit(instance=profile)      
    return render(request, 'accounts/profile_edit.html',{'user_form': user_form, 'profile_form': profile_form})

@login_required
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    query = request.GET.get("q")
    if query:
        songs = Song.objects.filter(Q(song_title__icontains=query)).distinct()
        if songs.count() == 0:
            messages.error(request, "No results found from your query. Please search different query")
        else:
            messages.success(request, "{} results found".format(songs.count()))
        return render(request,'music/all_songs.html',{'songs' : songs})
    return render(request, 'accounts/dashboard.html', {'profile' : profile})