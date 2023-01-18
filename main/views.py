from django.shortcuts import render, get_object_or_404
from .models import Person
from .forms import PersonForm


def home(request):
    return render(request, 'home.html')


def create_view(request):
    context = {}

    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create.html", context)


def retrieve_view(request):
    objects = Person.objects.all()
    return render(request, "retrieve.html", {'objects': objects})


def detail_view(request, id):
    object = get_object_or_404(Person, id=id)
    return render(request, 'deetail.html', {'object': object})


def update_view(request):
    return render(request, 'update.html')


def delete_view(request):
    return render(request, 'delete.html')
