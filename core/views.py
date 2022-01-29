from typing import List
from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import TemplateView , ListView , CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from core.models import Profile
from .forms import ProfileForm
from .models import Movie , Profile

class Home(TemplateView):
    def get(self , request , *args, **kwargs):
        return render(request , 'index.html')

@method_decorator(login_required,name='dispatch')
class ProfileList(ListView):
    def get(self , request , *args, **kwargs):
        profiles = request.user.profile.all()
        return render(request , 'profileList.html' , 
        {'profiles': profiles
        })


class ProfileCreate(CreateView):
    def get(self , request , *args, **kwargs):
        # todo form to create profile
       
        form = ProfileForm()
       
        return render(request , 'profileCreate.html' ,  context = {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None )

        if form.is_valid():
            print(form.cleaned_data)
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profile.add(profile)
                return redirect('core:profle_list')

        return render(request, 'profileCreate.html' , {
            'form': form
        })


method_decorator(login_required,name='dispatch')
class Watch(View):
    def get(self,request,profile_id,*args, **kwargs):
        try:
            profile=Profile.objects.get(uuid=profile_id)

            movies=Movie.objects.filter(age_limit=profile.age_limit)

            try:
                showcase=movies[0]
            except :
                showcase=None
            

            if profile not in request.user.profiles.all():
                return redirect(to='core:profile_list')
            return render(request,'movieList.html',{
            'movies':movies,
            'show_case':showcase
            })
        except Profile.DoesNotExist:
            return redirect(to='core:profile_list')





@method_decorator(login_required,name='dispatch')
class ShowMovieDetail(View):
    def get(self,request,movie_id,*args, **kwargs):
        try:
            
            movie=Movie.objects.get(uuid=movie_id)

            return render(request,'movieDetail.html',{
                'movie':movie
            })
        except Movie.DoesNotExist:
            return redirect('core:profile_list')


@method_decorator(login_required,name='dispatch')
class ShowMovie(View):
    def get(self,request,movie_id,*args, **kwargs):
        try:
            
            movie=Movie.objects.get(uuid=movie_id)

            movie=movie.videos.values()
            

            return render(request,'showMovie.html',{
                'movie':list(movie)
            })
        except Movie.DoesNotExist:
            return redirect('core:profile_list')