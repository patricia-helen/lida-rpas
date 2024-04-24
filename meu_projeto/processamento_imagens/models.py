# lida-rpas/meu_projeto/processamento_imagens/models.py
from django.db import models

class GeospatialImage(models.Model):
    # Armazena imagens carregadas pelo usuário
    image = models.ImageField(upload_to='geospatial_images/')
    # Data de upload automático
    upload_date = models.DateTimeField(auto_now_add=True)
    # Imagem processada após cálculos (opcional)
    ndvi_image = models.ImageField(upload_to='processed_images/', blank=True, null=True)
    # Descrição adicional (opcional)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Image {self.id} - {self.upload_date}"

    # Função para retornar o caminho completo da imagem NDVI
    def get_ndvi_image_url(self):
        return self.ndvi_image.url if self.ndvi_image else None
