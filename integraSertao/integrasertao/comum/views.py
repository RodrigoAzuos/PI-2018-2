from django.shortcuts import render, redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from comum.models import Post, AreaTematica

# Create your views here.

def index(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render(request, "index.html", {'posts': posts})

@login_required(login_url='/login')
def add_post(request):

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():

            model_instance = form.save(commit=False)
            model_instance.autor = request.user.perfil
            model_instance.save()
            return redirect('index')

        return render(request, "add-post.html", {'form': form})

    else:
        form = PostForm()
        return render(request, "add-post.html", {'form': form})

def exibir_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "post.html", {'post': post})

def index2(request):
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


    return render(request, "index2.html", {'principal': principal, 'posts': posts ,'areas_tematica': areas_tematica})



