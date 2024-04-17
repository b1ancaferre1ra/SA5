from django.shortcuts import render, redirect
from webCad.models import Pessoa

dados = []

# Create your views here.
def home(request):
    nome = ""
    email = ""
    data = ""
    pais = ""

    dados = Pessoa.objects.all().order_by('-id')[:10]

    if request.POST:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        data = request.POST.get("data")
        pais = request.POST.get("pais")
        Pessoa.objects.create(nome=nome, email=email, data=data, pais=pais)
        
    
    return render(request, "webCad/global/index.html", context={"dados":dados, "nome":nome, "email": email, "data": data, "pais":pais})

def cadastrar(request):
    nome = ""
    email = ""
    data = ""
    pais = ""

    if request.POST:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        data = request.POST.get("data")
        pais = request.POST.get("pais")
        Pessoa.objects.create(nome=nome, email=email, data=data, pais=pais)
        
    
    return render(request, "webCad/partials/cadastrar.html", context={"nome":nome, "email": email, "data": data, "pais":pais})

# O django "ignora" a pasta template, não é necessário colocá-la no caminho da página

def deletar(request, id=0):
    pessoa = {}
    if id:
        pessoa = Pessoa.objects.get(id=id)
        pessoa.delete()
        return redirect('deletar')
    
    nome_filter = request.GET.get("nome")
    if nome_filter:
        pessoa["pessoa"] = Pessoa.objects.filter(nome__icontains=nome_filter)
    else:
        pessoa["pessoa"] = Pessoa.objects.all()
    return render(request, "webCad/partials/deletar.html", context=pessoa)

def atualizar(request, id=0):
    pessoa = {}
    if id:
        if request.POST:
            pessoa = Pessoa.objects.get(id=id)
            pessoa.nome = request.POST.get("nome",pessoa.nome)
            pessoa.email = request.POST.get("email",pessoa.email)
            pessoa.data = request.POST.get("data",pessoa.data)
            pessoa.pais = request.POST.get("pais",pessoa.pais)

            pessoa.save()
            return redirect('atualizar')
        
        pessoa["pessoa"] = Pessoa.objects.get(id=id)
        return render (request, "webCad/partials/update.html", pessoa)
    
    nome_filter = request.GET.get("nome")
    if nome_filter:
        pessoa["pessoa"] = Pessoa.objects.filter(nome__icontains=nome_filter)
    else:
        pessoa["pessoa"] = Pessoa.objects.all()    
    
    return render(request, "webCad/partials/atualizar.html", context=pessoa)

def pesquisar(request):
    dados = {}
    if request.GET:
        nome_filter = request.GET.get("nome")
        dados["dados"] = Pessoa.objects.filter(nome__icontains=nome_filter)
    else:
        dados["dados"] = Pessoa.objects.all()
        
    return render(request, "webCad/partials/pesquisar.html", dados)