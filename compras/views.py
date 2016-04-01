from django.shortcuts import render

def compras_list(request):
        return render(request, 'compras/compras_list.html', {})
