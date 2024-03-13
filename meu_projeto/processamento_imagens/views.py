# processamento_imagens/views.py
from django.shortcuts import render
from .forms import ImageUploadForm
from .processamento import processar_imagem  # Suponha que você tem essa função

def upload_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            imagem = request.FILES['image']
            # Aqui você pode processar a imagem com sua função de processamento
            resultado = processar_imagem(imagem)  # Adapte essa função conforme necessário
            
            # Supondo que o processamento foi bem-sucedido e você quer notificar o usuário
            # Você pode querer retornar alguma informação específica do resultado
            # Para este exemplo, apenas retornaremos uma mensagem genérica
            mensagem_sucesso = "Imagem processada com sucesso!"
            
            # Alterado para passar a mensagem de sucesso ao template de resultado
            return render(request, 'processamento_imagens/resultado.html', {'resultado': mensagem_sucesso})
    else:
        form = ImageUploadForm()
    return render(request, 'processamento_imagens/upload.html', {'form': form})
