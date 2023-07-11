from django.db import models
from autoslug import AutoSlugField
from blog.models  import KategoriModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel

class YazılarModel (DateAbstractModel):
    resim=models.ImageField(upload_to='yazi_resimleri')
    baslik = models.CharField(max_length=50,null=False,blank=False)
    icerik = RichTextField()
   
    
    slug=AutoSlugField(populate_from='baslik',unique=True)
    kategoriler  = models.ManyToManyField(KategoriModel, related_name= 'yazi')
    #her yazının birden fazla kategorisi olabilir 
    #related name bir kategoriye ait tüm yazıları çekmek istediğimizde kullanılır
    yazar=models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yazilar')
    
    class Meta:
        verbose_name= 'Yazi'
        verbose_name_plural= 'Yazilar'
        db_table='Yazi'
        
    def __str__(self):
        return self.baslik
        
        
    
    