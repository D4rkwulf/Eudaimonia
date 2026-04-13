from django.shortcuts import render


def nutrition_builder(request):
    return render(request, 'nutrition/nutrition_builder.html')
