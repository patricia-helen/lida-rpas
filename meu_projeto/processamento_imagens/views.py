# lida_rpas/meu_projeto/processamento_imagens/views.py
from django.shortcuts import render, redirect
from .forms import UploadForm  # Import do formulário de upload
from .models import GeospatialImage  # Modelo para armazenar imagens geoespaciais
import rasterio
import numpy as np
import matplotlib.pyplot as plt

def home_page_view(request):
    # Renderiza a homepage com contexto adicional
    context = {
        'introduction': 'LIDA-RPAS é um laboratório dedicado à inovação e aplicação de sistemas de aeronaves remotamente pilotadas.',
        'project_image': 'LIDA.png'
    }
    return render(request, 'processamento_imagens/home.html', context)

def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()
            return redirect('image_result', image_instance.id)
    else:
        form = UploadForm()

    # Renderiza o template de upload com o formulário
    return render(request, 'processamento_imagens/upload.html', {'form': form})

def image_result(request, image_id):
    # Obtém a imagem processada e exibe os resultados
    geospatial_image = GeospatialImage.objects.get(id=image_id)
    context = {
        'image': geospatial_image,
        'ndvi_image_url': geospatial_image.get_ndvi_image_url(),
    }
    return render(request, 'processamento_imagens/resultado.html', context)

def calculate_ndvi(image_instance):
    # Calcula o NDVI para a imagem fornecida
    with rasterio.open(image_instance.image.path) as src:
        red = src.read(1)  # Canal vermelho
        nir = src.read(2)  # Canal infravermelho próximo

        ndvi = (nir - red) / (nir + red)  # Cálculo do NDVI

        output_path = f"processed_images/ndvi_{image_instance.id}.png"
        plt.imshow(ndvi, cmap='viridis')
        plt.colorbar()
        plt.savefig(output_path)  # Salva o resultado NDVI

        image_instance.ndvi_image = output_path
        image_instance.save()
