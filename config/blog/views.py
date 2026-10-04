from django.shortcuts import render, get_object_or_404
from .models import Post


def lista(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista.html', {'posts': posts})


def detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.all()
    contexto = {'post': post, 'comentarios': comentarios}
    return render(request, 'blog/detalle.html', contexto)