from .models import Category, Transaction
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound


# получение данных из бд
def index(request):
    current_user = request.user
    transactions = Transaction.objects.filter(user=current_user)
    categories = Category.objects.filter(user=current_user)
    return render(request, "main.html", {"categories": categories, 'transactions': transactions})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        current_user = request.user
        name = request.POST.get("name")
        category = Category.objects.create(name=name, user=current_user)
        category.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        category = Category.objects.get(id=id)

        if request.method == "POST":
            current_user = request.user
            category.name = request.POST.get("name")
            category.user = current_user
            category.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "categories/edit.html", {"category": category})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Категория не найдена</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        current_user = request.user
        category = Category.objects.get(id=id, user=current_user)
        category.delete()
        return HttpResponseRedirect("/")
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Категория не найдена</h2>")


def create_tr(request):
    current_user = request.user
    cat_for_transact = Category.objects.filter(user=current_user)
    if request.method == "POST":
        result = request.POST.get("cat_for_transact")
        amount = request.POST.get("amount")
        time = request.POST.get("time")
        organization = request.POST.get("organization")
        description = request.POST.get("description")
        date = request.POST.get("date")
        transaction = Transaction.objects.create(category_id=result, amount=amount, time=time,
                                                 organization=organization, description=description,
                                                 date=date, user=current_user)
        transaction.save()
        return HttpResponseRedirect("/")
    return render(request, "categories/create_transact.html", {"cat_for_transact": cat_for_transact})
