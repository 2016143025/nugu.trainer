from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import trainer
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

# Create your views here.


def home(request):
    latest_trainer_list = trainer.objects.all()
    template = loader.get_template('nuguhome/homepage.html')
    context = {
        'latest_trainer_list': latest_trainer_list,
    }
    return HttpResponse(template.render(context,request))

def write(request):
    return render(request,'nuguhome/write.html')

@csrf_exempt
def like(request):
    trainerone = trainer.objects.get(id=request.POST['hiddenlike'])
    if request.POST['btlike'] == '좋아요':
        trainerone.like +=1
        trainerone.save()
    else:
        trainerone.dislike+=1
        trainerone.save()
    latest_trainer_list = trainer.objects.all()
    template = loader.get_template('nuguhome/homepage.html')
    context = {
        'latest_trainer_list': latest_trainer_list,
    }
    return HttpResponse(template.render(context,request))

@csrf_exempt
def wrote(request):
    newtrainer = trainer(gym = request.POST['gym'],
                         name = request.POST['name'],
                         inform= request.POST['inform'])
    newtrainer.save()
    latest_trainer_list = trainer.objects.all()
    template = loader.get_template('nuguhome/homepage.html')
    context = {
        'latest_trainer_list': latest_trainer_list,
    }
    return HttpResponse(template.render(context,request))