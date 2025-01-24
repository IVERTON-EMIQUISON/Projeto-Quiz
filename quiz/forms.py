from django import forms  
from .models import Pergunta, Alternativa, Resposta  

class PerguntaForm(forms.ModelForm):  
    class Meta:  
        model = Pergunta  
        fields = ['texto']  

class AlternativaForm(forms.ModelForm):  
    class Meta:  
        model = Alternativa  
        fields = ['texto', 'correta']  

class RespostaForm(forms.ModelForm):  
    class Meta:  
        model = Resposta  
        fields = ['alternativa']  # Aqui você deve ajustar para usar a sua lógica de resposta