from django.shortcuts import render


def articles(request):
    return render(request, 'content/articles.html')


def article_detail(request):
    return render(request, 'content/article_detail.html')
