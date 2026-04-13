from django.shortcuts import render


def workout_builder(request):
    return render(request, 'training/workout_builder.html')
