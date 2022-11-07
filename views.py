import json
from tkinter.messagebox import QUESTION
from django.forms import model_to_dict
from django.http import HttpResponse, Http404, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from .models import Question
import logging
from django.shortcuts import render, get_object_or_404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


@csrf_exempt
def all(request):
    if request.method == 'GET':
        return JsonResponse ({
            'Question' : [
                question.to_dict() for question in Question.objects.all()
            ]
        })
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        client = Question.objects.create(
            question_text = data['question_text'],
            pub_date = data['date_pub']
        )
        client.save()
        return JsonResponse ({
            'data'  : [data['question_text']]
        })
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        client = Question.objects.get(question_text= data['old_text'])
        if (len(data) > len(client.to_dict())):
            client.question_text = data['question_text']
            client.pub_date = data['date_pub']
            client.save()
        return JsonResponse ({
            'Question' : [
                data
            ]
        })
    elif request.method == 'DELETE':
        data = json.loads(request.body.decode('utf-8'))
        Question.objects.get( question_text = data['question_text']).delete()