from django.shortcuts import render, redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from comum.models import Post, AreaTematica

# Create your views here.

def index(request):
    principal = Post.objects.all().order_by('-criado_em')[:3]
    posts_list = Post.objects.all()
    areas_tematica = AreaTematica.objects.all().order_by('-nome')
    paginator = Paginator(posts_list, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    log = logado(request)

    return render(request, "index2.html", {'principal': principal, 'posts': posts ,'areas_tematica': areas_tematica, 'logado':log})

@login_required(login_url='/login')
def add_post(request):
    log = logado(request)
    areas_tematica = AreaTematica.objects.all().order_by('-nome')
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():

            model_instance = form.save(commit=False)
            model_instance.autor = request.user.perfil
            model_instance.save()
            return redirect('index')

        return render(request, "add-post.html", {'form': form,'areas_tematica': areas_tematica, 'logado':log})

    else:
        form = PostForm()
        return render(request, "add-post.html", {'form': form,'areas_tematica': areas_tematica, 'logado':log})

def exibir_post(request, post_id):
    areas_tematica = AreaTematica.objects.all().order_by('-nome')
    post = Post.objects.get(pk=post_id)

    log = logado(request)
    return render(request, "post.html", {'post': post, 'areas_tematica': areas_tematica, 'logado':log})

def buscar(request, palavra_chave):
    areas_tematica = AreaTematica.objects.all().order_by('-nome')
    posts_list = Post.objects.filter(palavras_chave__icontains = palavra_chave)
    paginator = Paginator(posts_list, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    log = logado(request)
    return render(request, "search.html", {'posts': posts, 'areas_tematica': areas_tematica,'logado':log})

def filtrar_categoria(request, categoria_id):
    principal = Post.objects.all().order_by('-criado_em')[:3]
    posts_list = Post.objects.filter(area_tematica__pk=categoria_id)
    areas_tematica = AreaTematica.objects.all().order_by('-nome')
    paginator = Paginator(posts_list, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    log = logado(request)
    return render(request, "index2.html",
                  {'principal': principal, 'posts': posts, 'areas_tematica': areas_tematica, 'logado': log})

def like(request, post_id):

    post = Post.objects.filter(pk=post_id)
    post.like(request.user.perfil)

    return redirect('index post_id')


def deslike(request, post_id):
    post = Post.objects.filter(pk=post_id)
    post.deslike(request.user.perfil)

    return redirect('index post_id')

<<<<<<< HEAD
def search(request, palavra_chave):

    posts_list = Post.objects.filter(palavras_chave__icontains = palavra_chave)
    paginator = Paginator(posts_list, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render(request, "search.html", {'posts': posts})

def like(request, post_id):

    post = Post.objects.filter(pk=post_id)
    post.like(request.user.perfil)

    return redirect('index post_id')


def deslike(request, post_id):
    post = Post.objects.filter(pk=post_id)
    post.deslike(request.user.perfil)

    return redirect('index post_id')
=======
def logado(request):

    if request.user.id:
        return True
    return False
>>>>>>> 969422aa502f3d6bdf22fdb237a4a0c276fc6f64
