from django.shortcuts import render
from app.forms import EmpresaForm

# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_contato(request):
    formulario = EmpresaForm(request.POST or None)
    msg = ''

    if formulario.is_valid():
        formulario.save()
        formulario = EmpresaForm()
        msg = 'Cadastro realizado com sucesso'

    contexto = {
        'form' : formulario,
        'msg' : msg
    }
    return render(request, 'contato.html', contexto)