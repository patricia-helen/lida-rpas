# Verifique se a importação é correta
from django.urls import path  # Certifique-se de que as importações essenciais estão presentes
from django.contrib import admin  # Importação para a rota do admin
from processamento_imagens.views import home_page_view, upload_view  # Importação para views corretas

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para a página do admin
    path('', home_page_view, name='home'),  # Rota para a página inicial
    path('upload/', upload_view, name='upload_image'),  # Rota para a página de upload
]
