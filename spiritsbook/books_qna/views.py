from django.shortcuts import render
from .models import Questions_Answer
from random import randint


def home(request):
    qna_list = Questions_Answer.objects.all()
    count = Questions_Answer.objects.count()
    qrandom = int(str(Questions_Answer.objects.all()[randint(0, count - 1)]))
    return render(request, 'home.html', {'qna_list': qna_list, 'qrandom': qrandom})

def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results_qnumber = Questions_Answer.objects.filter(qnumber__contains=searched)
        results_questions = Questions_Answer.objects.filter(question__icontains=searched)
        results_answers = Questions_Answer.objects.filter(answer__icontains=searched)
        results_notes = Questions_Answer.objects.filter(note__icontains=searched)
        return render(request, 'search_results.html', {
            'searched': searched, 'results_qnumber': results_qnumber,
            'results_questions': results_questions, 'results_answers': results_answers,
            'results_notes': results_notes,
        })
    else:
        return render(request, 'search_results.html', {})
