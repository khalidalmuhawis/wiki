from django.shortcuts import render
from pages.models import Page

def pages_list(request):
    pages = Page.objects.all()
    context = {
    'pages': pages
    }


    return render(request, 'list.html', context)


def pages_detail(request, page_id):
    page = Page.objects.get(id=page_id)
    context = {
    'page': page
    }

    return render(request, 'detail.html', context)
