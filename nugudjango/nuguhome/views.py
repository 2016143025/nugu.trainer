from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import trainer
# Create your views here.


def home(request):
    latest_trainer_list = trainer.objects.all()
    template = loader.get_template('nuguhome/homepage.html')
    context = {
        'latest_trainer_list': latest_trainer_list,
    }
    return HttpResponse(template.render(context,request))
