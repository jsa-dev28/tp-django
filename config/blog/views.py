from django.shortcuts import render, redirect, get_object_or_404

from .forms import ComentarioForm
from .models import Post

def lista(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista.html', {'posts': posts})

def detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('blog:detalle', pk=post.pk)
    else:
        form = ComentarioForm()

    contexto = {
        'post': post,
        'comentarios': post.comentarios.all(),
        'form': form,
    }
    return render(request, 'blog/detalle.html', contexto)