from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def home(requset):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(requset,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':movie})
def addmovie(request):
    if request.method =='POST':
        moviename=request.POST.get('moviename',)
        director= request.POST.get('director',)
        industry = request.POST.get('industry',)
        genre = request.POST.get('genre',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movie=Movie(moviename=moviename,director=director,industry=industry,genre=genre,desc=desc,year=year,img=img)
        movie.save()

    return render(request,"addmovie.html")

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")

