from django.db import models


class Questions_Answer(models.Model):
    qnumber = models.IntegerField()
    question = models.TextField('Question', blank=True)
    answer = models.TextField('Answer', blank=True)
    note = models.TextField('Notes', blank=True)

    def __str__(self):
        return self.qnumber
