from django.db import models


# class Questions(models.Model):
#     question = models.TextField('Question', blank=True)
#
#     def __str__(self):
#         return self.question
#
#
# class Answers(models.Model):
#     answer = models.TextField('Answer', blank=True)
#
#     def __str__(self):
#         return self.answer
#
#
# class Notes(models.Model):
#     note = models.TextField('Notes', blank=True)
#
#     def __str__(self):
#         return self.note
#

class Questions_Answer(models.Model):
    qnumber = models.CharField('Question number', max_length=10)
    question = models.TextField('Question', blank=True)
    answer = models.TextField('Answer', blank=True)
    note = models.TextField('Notes', blank=True)

    def __str__(self):
        return self.qnumber
