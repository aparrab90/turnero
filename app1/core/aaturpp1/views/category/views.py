from django.shortcuts import render

from core.aaturpp1.models import Category


def category_lis(request):
    data = {
        'title': 'Listado de Categorias',
        'categories': Category.objects.all

    }
    return render(request, 'category/list.html', data)