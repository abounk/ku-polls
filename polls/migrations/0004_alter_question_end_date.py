# Generated by Django 3.2.7 on 2021-09-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_question_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
