from django.shortcuts import render, get_object_or_404
from .forms import ObitForm
from .models import Obit


def home(request):
    return render(request, 'home.html')


def logged_home(request):
    return render(request, 'logged_home.html')


def obit_form(request):
    form = ObitForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ObitForm()
    return render(request, 'create_obit.html', {'form': form})


def search_obit(request):
    filt = request.GET.get('q', '')
    q_set = Obit.objects.filter(last_name__iexact=filt)
    context = {
        "obit_set": q_set
    }
    print(q_set)

    return render(request, 'search_obit.html', context)


def obit_detail(request, id):
    obj = get_object_or_404(Obit, id=id)
    context = {
        'obit': obj
    }
    return render(request, 'obit_details.html', context)


def my_account(request):
    return render(request, 'my_account.html')


def comp_details(request):
    return render(request, 'comp_details.html')


def comp_list(request):
    return render(request, 'comp_list.html')