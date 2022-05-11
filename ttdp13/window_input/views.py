import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from .models import *
from .forms import Input_text_and_save


menu = [
    {'title': 'form input', 'url_str': 'win_inp'},
    {'title': 'list input', 'url_str': 'list_inp'}
]



def win_inp(request):
    list_name = ['input_1']
    # Условие для очистки БД
    wi = WindowInput.objects.all()
    if len(wi) > len(request.POST):
        wi.delete()
    # Счетчик input'ов всегда на один больше от числа записей в БД
    counter_input_block = len(WindowInput.objects.all()) + 2

    if request.method == 'POST':
        form = Input_text_and_save(request.POST, counter_input=counter_input_block)
        if form.is_valid():

            name_in = "input_" + str(len(request.POST) - 1)
            list_name.append(name_in)
            dt_in = form.cleaned_data.get(name_in)
            dt_in = json.dumps(dt_in, ensure_ascii=False, sort_keys=True, indent=4)
            print(dt_in)
            form = Input_text_and_save(request.POST, counter_input=len(request.POST) + 1)

            WindowInput.objects.create(text_input=dt_in).save()


    else:
        form = Input_text_and_save(request.POST, counter_input=counter_input_block)
    context = {"menu": menu,
               "title": menu[0]['title'],
               "url_str": menu[0]['url_str'],
               "form": form,
               "list_name": list_name
    }
    return render(request, "window_input/main.html", context=context)


def list_input(request):
    text_input = list(WindowInput.objects.all().values())
    context = {"menu": menu,
               "title": menu[1]['title'],
               "url_str": menu[1]['url_str'],
               "text_input": text_input
               }

    return render(request, "window_input/list_input.html", context=context)
    # return JsonResponse(context, safe=False,)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
