from django.urls import path
from .views import cadastrar_pergunta, cadastrar_alternativa, responder_pergunta, list_perguntas, create_pergunta, list_alternativas, create_alternativa

urlpatterns = [
    path('cadastrar-pergunta/', cadastrar_pergunta, name='cadastrar_pergunta'),
    path('cadastrar-alternativa/', cadastrar_alternativa, name='cadastrar_alternativa'),
    path('responder-pergunta/', responder_pergunta, name='responder_pergunta'),
    path('perguntas/', list_perguntas, name='list_perguntas'),  # List all questions
    path('perguntas/create/', create_pergunta, name='create_pergunta'),  # Create a new question
    path('perguntas/<int:id>/alternativas/', list_alternativas, name='list_alternativas'),  # List alternatives for a specific question
    path('perguntas/<int:id>/alternativas/create/', create_alternativa, name='create_alternativa'),  # Create a new alternative for a specific question
]
