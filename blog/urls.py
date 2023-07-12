

from django.urls import path

from blog.views import iletisim , anasayfa , kategori , yazilarim







urlpatterns = [
    path('', anasayfa , name = 'anasayfa'),
    path('iletisim/', iletisim , name = 'iletisim'),
    path('kategori/<slug:KategoriSlug>', kategori , name = 'kategori'),
    path('yazilarim/' , yazilarim , name= 'yazilarim')
]
