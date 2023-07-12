
from django.contrib import admin
from django.urls import path  , include
from blog.views import iletisim
from django.conf.urls.static import static
from django.conf import settings






urlpatterns = [
    path('admin/', admin.site.urls),
    #path('blog/iletisim/', iletisim),
    path('', include('blog.urls')) # 'blog/' vardı
    #path in icinde blog yerine '' seklinde boş bırakırsak o sayfa anasayfa olur
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
