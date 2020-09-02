from django.shortcuts import render, redirect
from .models import Food, Consume


# Create your views here.


def index(request):

    if request.method == "POST":
        food_consumed = request.POST.get("food_consumed")
        consume = Food.objects.get(name=food_consumed)

        # user acutellement connecté à l'origine de la requête
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()

    consumed_food = Consume.objects.filter(user=request.user)
    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})


def delete_consumed(request, consumed_id):
    consumed_food = Consume.objects.get(id=consumed_id)
    if request.method == "POST":
        consumed_food.delete()
        return redirect('/')

    return render(request, 'myapp/delete.html')

