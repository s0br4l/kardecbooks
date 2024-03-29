from django.shortcuts import render
from .models import Questions_Answer
from random import choice


def home(request):
    qna_list = Questions_Answer.objects.all()
    qrandom = choice(list(qna_list))

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

def qnalist(request):
    qnalist = Questions_Answer.objects.all()
    return render(request, 'qnalist.html', {'qnalist': qnalist, })

def qnaid(request, qna_id):
    qnaid = Questions_Answer.objects.get(pk=qna_id)
    return render(request, 'qna.html', {'qnaid': qnaid, })

