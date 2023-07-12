from django.shortcuts import render , get_object_or_404
from blog.models import YazılarModel , KategoriModel
from django.core.paginator import Paginator


def kategori(request , KategoriSlug):
        kategori = get_object_or_404(KategoriModel , slug = KategoriSlug)
        yazilar = kategori.yazi.all(
        print(yazilar)
        )
        sayfa = request.GET.get(' sayfa')
        paginator = Paginator( yazilar , 1)
        

        
       
        
        return render(request , 'pages/kategori.html' , context={
                'yazilar' : paginator.get_page(sayfa)
        })