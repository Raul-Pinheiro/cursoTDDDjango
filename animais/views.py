from django.shortcuts import render
from animais.models import Animais

def index(request):
    animais = Animais.objects.all()
    context = {
        'title':'Busca Animal',
        'caracteristicas': animais,
    }

    if 'buscar' in request.GET:
        animal_pesquisado = request.GET['buscar']
        caracteristicas = animais.filter(nome_animal__icontains = animal_pesquisado)

        context['caracteristicas'] = caracteristicas

    
    return render(request, 'index.html', context)