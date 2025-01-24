# quiz/urls.py  

from django.urls import path
from .views import cadastrar_pergunta, cadastrar_alternativa, responder_pergunta

urlpatterns = [
    path('cadastrar-pergunta/', cadastrar_pergunta, name='cadastrar_pergunta'),
    path('cadastrar-alternativa/<int:pergunta_id>/', cadastrar_alternativa, name='cadastrar_alternativa'),
    path('responder-pergunta/<int:pergunta_id>/', responder_pergunta, name='responder_pergunta'),
]
