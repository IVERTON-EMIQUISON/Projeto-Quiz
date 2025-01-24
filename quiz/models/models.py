from django.db import models  
from django.contrib.auth.models import User  

class Pergunta(models.Model):  
    texto = models.CharField(max_length=255)  
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):  
        return self.texto  

class Alternativa(models.Model):  
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)  
    texto = models.CharField(max_length=255)  
    correta = models.BooleanField(default=False)  

    def __str__(self):  
        return self.texto  

class Resposta(models.Model):  
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)  
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  
    alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE)  

    def __str__(self):  
        return f'{self.usuario.username} respondeu: {self.alternativa.texto}'