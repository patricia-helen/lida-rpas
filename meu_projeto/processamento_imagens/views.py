# processamento_imagens/views.py
from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .processamento import processar_imagem  # Função adaptada do seu notebook

def upload_and_process(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            imagem = request.FILES['image']
            
            # Aqui você adaptaria o processamento para trabalhar com o arquivo carregado
            # Por exemplo, salvar temporariamente e processar
            resultado = processar_imagem(imagem)  # Adapte essa função conforme necessário

            # Você pode querer redirecionar para uma nova página com o resultado
            # ou passar o resultado para o template
            return render(request, 'resultado.html', {'resultado': resultado})
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})
