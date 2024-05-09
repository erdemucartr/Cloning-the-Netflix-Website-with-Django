from django.shortcuts import render,redirect
from .models import *
from user.models import *
from django.db.models import Q
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('profil')
    return render(request,'index.html')


def movie(request,id):
    profil = Profil.objects.get(id = id)
    profiller = request.user.profil_set.all()
    filmler = Movie.objects.all()
    kategori = Category.objects.get(title = 'Komedi')
    komediFilm = Movie.objects.filter(category = kategori)
    context = {
        'filmler':filmler,
        'komediFilm':komediFilm,
        'profiller':profiller,
        'profil':profil
    }
    return render(request,'movie.html',context)


def movieDetail(request,d_slug):
    
    film = Movie.objects.get(slug = d_slug)
    # ! Get ile çektiğimiz obje doğrudan bize döner, sayfada çağırırken For döngüsüne ihtiyaç duymayız.
    # film = Movie.objects.filter(slug = d_slug)
    # ! Filter kullanırken obje bir query set halinde dönder , sayfada for döngüsü ile çağırmamız gerekir.
    context = {
        'film':film
    }
    return render(request,'movieDetay.html',context)


def search(request): 
    if 'search' in request.GET and request.GET.get('search'):
        # Eğer 'search' anahtarı request.GET olan formda mevcutsa ve aynı zamanda inputum boş değilse:
        ara = request.GET.get('search')
        # 'search' edilen bilgiyi al ve ara değişkenenine at
       
        filmler = Movie.objects.filter(
            Q(title__icontains=ara) |
            Q(description__icontains=ara) 
            
        )
        # Ve movie modelindeki titleı benim ara değişkenimin içinde olan yapıyla filtrele
    else:
        ara = request.GET.get('search')

    tumFilmler = Movie.objects.all()
    context = {
        'filmler':filmler,
        'ara':ara,
        'tumFilmler':tumFilmler
    }   
        

    return render(request,'search.html',context)


def favoriler(request):
    favoriler = Favoriler.objects.filter(user = request.user)
    context = {
        'favoriler':favoriler
    }
    return render(request,'favoriler.html',context)

from django.http import HttpResponse
def favoriEkle(request):
    if request.method == 'POST':
        favori_id = request.POST.get('film_id')
        film = Movie.objects.get(id = favori_id)

        varmı = Favoriler.objects.filter(user = request.user ,film = film).exists()
        # Kullanıcı bu filmi favorilerine eklemiş mi eklememiş mi,
        if varmı:
            return HttpResponse('Bu film favorilere eklenmiş')
        else:
            Favoriler.objects.create(user = request.user,film = film)
            return redirect('favoriler')
        


    
