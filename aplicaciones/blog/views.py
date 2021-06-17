from django.shortcuts import get_object_or_404, render 
from .models import Categoria, Post
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    #print (request.GET)    
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True)
    #print (queryset)
    if queryset :
        posts= Post.objects.filter(
            Q(titulo__icontains= queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
    #----------------------------------------
    paginator= Paginator(posts,2)
    page= request.GET.get('page')
    posts= paginator.get_page(page)
    #-----------------------------------
    return render(request,'index.html',{'posts':posts})

def generales(request):
    queryset= request.GET.get("buscar")
    posts= Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre__iexact= "General"))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains= queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=  Categoria.objects.get(nombre__iexact= "General")
        ).distinct()
    #----------------------------------------
    paginator= Paginator(posts,2)
    page= request.GET.get('page')
    posts= paginator.get_page(page)
    #-----------------------------------
    return render(request,'generales.html',{'posts':posts})

def detallePost(request,slug):
    #post= Post.objects.get(slug = slug)
    post= get_object_or_404(Post,slug=slug)
    return render(request,'post.html', {'detalle_post':post})

def programacion(request):
    queryset= request.GET.get("buscar")
    posts= Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre__iexact= "Programación"))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria= Categoria.objects.get(nombre__iexact= "Programación")
        )
    #----------------------------------------
    paginator= Paginator(posts,2)
    page= request.GET.get('page')
    posts= paginator.get_page(page)
    #-----------------------------------
    return render(request,'programacion.html',{'posts':posts})

def videojuegos(request):
    queryset= request.GET.get('buscar')
    posts= Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre__iexact= "Videojuegos"))
    if queryset:
        posts= Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria= Categoria.objects.get(nombre__iexact= "Videojuegos")
        )
    #----------------------------------------
    paginator= Paginator(posts,2)
    page= request.GET.get('page')
    posts= paginator.get_page(page)
    #-----------------------------------
    return render(request,"videojuegos.html",{'posts':posts})

def tecnologia(request):
    queryset= request.GET.get('buscar')
    posts= Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre__iexact= "Tecnología"))
    if queryset:
        posts= Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria= Categoria.objects.get(nombre__iexact= "Tecnología")
        )
    #----------------------------------------
    paginator= Paginator(posts,2)
    page= request.GET.get('page')
    posts= paginator.get_page(page)
    #-----------------------------------
    return render(request,"tecnologia.html",{'posts':posts})

def tutoriales(request):
    queryset= request.GET.get('buscar')
    posts= Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre__iexact= "Tutoriales"))
    if queryset:
        posts= Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria= Categoria.objects.get(nombre__iexact= "Tutoriales")
        )
    #----------------------------------------
    paginator= Paginator(posts,2)
    page= request.GET.get('page')
    posts= paginator.get_page(page)
    #-----------------------------------
    return render(request,"tutoriales.html",{'posts':posts})