# Generated by Django 3.1.5 on 2021-01-19 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0005_auto_20210119_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_set',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='answers.surveyeesurvey', verbose_name='Набор ответов'),
        ),
    ]
