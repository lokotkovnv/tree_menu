from django.shortcuts import render


def page_view(request, page_name=None):
    return render(request, 'menu/base.html', {'page_name': page_name})
