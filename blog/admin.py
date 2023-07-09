from django.contrib import admin
from blog.models import KategoriModel
from blog.models import YazılarModel
from blog.models import YorumModel
from blog.models import IletisimModel
# Register your models here.
admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik' , 'icerik')
    list_display = (
        'baslik','olusturulma_tarihi','duzenlenme_tarihi'
    )
admin.site.register(YazılarModel, YazilarAdmin)

class YorumlarAdmin ( admin.ModelAdmin):
    search_fields =('yazan__username' , )
    list_display = (
        'yorum' , 'olusturulma_tarihi' , 'guncellenme_tarihi'
    ) 
admin.site.register(YorumModel, YorumlarAdmin)

class IletisimAdmin(admin.ModelAdmin):
    search_fields = ('email' , )
    list_display = (
        'email','olusturulma_tarihi')
admin.site.register(IletisimModel, IletisimAdmin)