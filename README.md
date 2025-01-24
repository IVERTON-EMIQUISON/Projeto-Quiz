# Projeto-Quiz
================
### Descrição
Um projeto de quiz que testa conhecimentos em diversas áreas, como história, ciência.

### Objetivos

- Criar um quiz com perguntas de diferentes áreas.
- Testar conhecimentos em diversas áreas.
- Melhorar habilidades de resolução de problemas.

### Funcionalidades

- Perguntas com múltiplas respostas.
- Opções de respostas correta e incorreta.
- Pontuação para cada resposta correta.
- Pontuação para cada resposta incorreta.

### Tecnologias utilizadas

- Python
- Tkinter

### Exemplo de uso

python
import tkinter as tk
from tkinter import messagebox
class Quiz: 
def __init__(self):
self.perguntas = [ 
    {'pergunta': 'Qual é a capital do Brasil?', 'opcoes': ['São Paulo ', 'Rio de Janeiro', 'Brasília', 'Salvador'], 'resposta': 3},]

def main(): 
root = tk.Tk()
root.title("Quiz")
app = Quiz()

### Como compilar o projeto

Para compilar o projeto, você precisará ter o Python instalado em sua máquina. Em seguida, abra o terminal e navegue até a pasta do projeto. Em seguida, execute o comando `python quiz.py` para iniciar o quiz. 

### Como executar o projeto

1. Instale o Python em sua máquina.
2. Abra o terminal e navegue até a pasta do projeto.
3. Execute o comando `python quiz.py` para iniciar o quiz.
