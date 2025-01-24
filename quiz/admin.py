from django.contrib import admin
from .models import Pergunta, Alternativa, Resposta

# Register your models here.
admin.site.register(Pergunta)
admin.site.register(Alternativa)
admin.site.register(Resposta)
