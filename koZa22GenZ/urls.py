"""koZa22GenZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from koZa.views import mainview
from koZa.views import hodowcy
from koZa.views import aboutus
from koZa.views import DodajHodowceWidok
from koZa.views import DodajTrawnikWidok
from koZa.views import trawniki
from koZa.views import najemkoz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainview),
    path('hodowcy/', hodowcy),
    path('aboutus/', aboutus),
    path('dodajhodowce/', DodajHodowceWidok.as_view()),
    path('dodajtrawnik/', DodajTrawnikWidok.as_view()),
    path('najemkoz/', najemkoz),
    #path('dodajtrawnik/', dodajtrawnik),
    path('trawniki/', trawniki),
]
