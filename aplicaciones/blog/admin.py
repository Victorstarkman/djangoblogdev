from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model =Categoria
class AutorResource(resources.ModelResource):
    class Meta:
        model =Autor
class PostResource(resources.ModelResource):
    class Meta:
        model=Post

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields =['nombre']
    list_display=('nombre','fecha_creacion','estado',)
    resource_class=CategoriaResource

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['nombres','apellidos','correo']
    list_display= ('apellidos','nombres','correo','fecha_creacion','estado',)
    resource_class=AutorResource

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['slug','titulo']
    list_display=('titulo','slug','descripcion','autor','categoria','estado',)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post,PostAdmin)
# Register your models here.
