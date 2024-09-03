from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AlunoForm
from .models import aluno

# Create your views here.
def index(request):
    alunos = aluno.objects.all()

    context = {
        "alunos": alunos
    }

    return render(request, 'index.html', context)

def cadastro(request):
    if request.method == 'POST':
        post_form = AlunoForm(request.POST)

        if post_form.is_valid():
            aluno.objects.create(**post_form.cleaned_data)

            return redirect(to='/')

    form = AlunoForm()

    context = {
        "form": form
    }

    return render(request, 'cadastro.html', context)