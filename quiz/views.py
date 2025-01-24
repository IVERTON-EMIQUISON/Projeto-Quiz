from django.shortcuts import render, redirect  
from django.contrib.auth.decorators import login_required  
from .models import Pergunta, Alternativa, Resposta  
from .forms import PerguntaForm, AlternativaForm, RespostaForm  

@login_required  
def cadastrar_pergunta(request):  
    if request.method == "POST":  
        form = PerguntaForm(request.POST)  
        if form.is_valid():  
            pergunta = form.save(commit=False)  
            pergunta.usuario = request.user  
            pergunta.save()  
            return redirect('cadastrar_pergunta')  
    else:  
        form = PerguntaForm()  
    return render(request, 'quiz/cadastrar_pergunta.html', {'form': form})  

@login_required  
def cadastrar_alternativa(request, pergunta_id):  
    pergunta = Pergunta.objects.get(id=pergunta_id)  
    if request.method == "POST":  
        form = AlternativaForm(request.POST)  
        if form.is_valid():  
            alternativa = form.save(commit=False)  
            alternativa.pergunta = pergunta  
            alternativa.save()  
            return redirect('cadastrar_alternativa', pergunta_id=pergunta.id)  
    else:  
        form = AlternativaForm()  
    return render(request, 'quiz/cadastrar_alternativa.html', {'form': form, 'pergunta': pergunta})  

@login_required  
def responder_pergunta(request, pergunta_id):  
    pergunta = Pergunta.objects.get(id=pergunta_id)  
    if request.method == "POST":  
        form = RespostaForm(request.POST)  
        if form.is_valid():  
            resposta = form.save(commit=False)  
            resposta.pergunta = pergunta  
            resposta.usuario = request.user  
            resposta.save()  
            return redirect('responder_pergunta', pergunta_id=pergunta_id)  
    else:  
        form = RespostaForm()  
    return render(request, 'quiz/responder_pergunta.html', {'form': form, 'pergunta': pergunta})  

@login_required
def list_perguntas(request):
    perguntas = Pergunta.objects.all()
    return render(request, 'quiz/list_perguntas.html', {'perguntas': perguntas})

@login_required
def create_pergunta(request):
    if request.method == "POST":
        form = PerguntaForm(request.POST)
        if form.is_valid():
            pergunta = form.save(commit=False)
            pergunta.usuario = request.user
            pergunta.save()
            return redirect('list_perguntas')
    else:
        form = PerguntaForm()
    return render(request, 'quiz/create_pergunta.html', {'form': form})

@login_required
def list_alternativas(request, pergunta_id):
    pergunta = Pergunta.objects.get(id=pergunta_id)
    alternativas = Alternativa.objects.filter(pergunta=pergunta)
    return render(request, 'quiz/list_alternativas.html', {'alternativas': alternativas, 'pergunta': pergunta})

@login_required
def create_alternativa(request, pergunta_id):
    pergunta = Pergunta.objects.get(id=pergunta_id)
    if request.method == "POST":
        form = AlternativaForm(request.POST)
        if form.is_valid():
            alternativa = form.save(commit=False)
            alternativa.pergunta = pergunta
            alternativa.save()
            return redirect('list_alternativas', pergunta_id=pergunta.id)
    else:
        form = AlternativaForm()
    return render(request, 'quiz/create_alternativa.html', {'form': form, 'pergunta': pergunta})
