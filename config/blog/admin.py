from django.contrib import admin
from .models import Post, Comentario


class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'creado']
    inlines = [ComentarioInline]


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['autor', 'post', 'creado']


admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)