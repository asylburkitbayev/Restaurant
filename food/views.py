from django.shortcuts import render
from .models import Category, Food, Table, BookTable, Response, Event


def home(request):
    return render(request, 'home.html')


def menu_category(request, id):
    foods = Food.objects.filter(category__id=id)
    categories = Category.objects.all()
    context = {
        'foods': foods,
        'categories': categories,
    }
    return render(request, 'menu.html', context)


def menu(request):
    foods = Food.objects.all()
    categories = Category.objects.all()
    context = {
        'foods': foods,
        'categories': categories,
    }
    return render(request, 'menu.html', context)


def booktable(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        table = request.POST['table']
        phone = request.POST['phone']
        persons = request.POST['persons']
        message = request.POST['message']

        book = BookTable.objects.create(
            name=name,
            email=email,
            table=Table.objects.get(id=table),
            phone=phone,
            persons=persons,
            message=message)
        book.save()
    tables = Table.objects.all()
    return render(request, 'booktable.html', {'tables': tables})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        subjects = request.POST['subjects']
        message = request.POST['message']

        response = Response.objects.create(
            name=name,
            phone=phone,
            email=email,
            subjects=subjects,
            message=message)
        response.save()
    return render(request, 'contact.html')


def event(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})
