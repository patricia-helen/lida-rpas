from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .processamento import processar_imagem

def home_page_view(request):
    # Esta linha agora está corretamente alinhada com o início da definição da função.
    return render(request, 'processamento_imagens/home.html')

def upload_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            imagem = request.FILES['image']
            
            # Processa a imagem usando sua função personalizada.
            resultado, imagem_processada_url = processar_imagem(imagem)

            # Passa o resultado e a URL da imagem processada para o template de resultado.
            context = {
                'resultado': resultado,
                'imagem_processada_url': imagem_processada_url,
            }
            return render(request, 'processamento_imagens/resultado.html', context)
    else:
        form = ImageUploadForm()

    return render(request, 'processamento_imagens/upload.html', {'form': form})
