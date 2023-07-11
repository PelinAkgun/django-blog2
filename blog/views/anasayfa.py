from django.shortcuts import render



def anasayfa(request):
    
        context = {
        'isim' : 'Pelin Akgun'
        }
        return render(request , 'pages/anasayfa.html' , context=context)