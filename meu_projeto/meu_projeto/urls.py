# meu_projeto/meu_projeto/urls.py
from django.contrib import admin
from django.urls import path
from processamento_imagens import views as processamento_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', processamento_views.home_page_view, name='home'),
    # Se você tiver outras URLs, adicione-as aqui
    path('upload/', processamento_views.upload_view, name='upload_image'),
]
