# Generated by Django 4.0.5 on 2022-06-30 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_qna', '0004_alter_questions_answer_qnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions_answer',
            name='qnumber',
            field=models.IntegerField(),
        ),
    ]
