from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from movieapp.models import Movie
from django.views import View
from movieapp.forms import MovieForm
from django.contrib import messages



class MovieCreateView(View):
    template_name = "movieapp/add.html"
    form = MovieForm

    def get(self, request):
        args = {"form":self.form}
        return render(request, self.template_name, args)
        
    def post(self, request):
        form = self.form(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie Created Successfully'>")
            return HttpResponseRedirect(reverse('create_movie'))
        return HttpResponseRedirect(reverse('create_movie'))


class MovieListView(View):
    template_name = "movieapp/list.html"

    def get(self, request):
        movies = Movie.objects.filter()
        args = {"movies":movies}
        return render(request, self.template_name, args)
        