# Generated by Django 3.2.4 on 2021-06-27 11:18

from django.db import migrations, models
import django.db.models.deletion
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_alter_question_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerSet',
            fields=[
                ('id', hashid_field.field.BigHashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', auto_created=True, min_length=13, prefix='', primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.survey', verbose_name='Анкета')),
            ],
            options={
                'verbose_name': 'Набор ответов',
                'verbose_name_plural': 'Наборы ответов',
            },
        ),
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.TextField(blank=True, help_text='Каждый вариант ответа вводить с новой строки.Оставить поле пустым, если выбран тип ответа в свободной форме', max_length=500, null=True, verbose_name='Варианты ответа'),
        ),
        migrations.CreateModel(
            name='AnswerSubset',
            fields=[
                ('id', hashid_field.field.BigHashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', auto_created=True, min_length=13, prefix='', primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.section', verbose_name='Секция')),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.answerset', verbose_name='Нпбор ответов')),
            ],
            options={
                'verbose_name': 'Набор ответов на секцию',
                'verbose_name_plural': 'Наборы ответов на секцию',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', hashid_field.field.BigHashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', auto_created=True, min_length=13, prefix='', primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, max_length=500, null=True, verbose_name='Ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.question', verbose_name='Вопрос')),
                ('subset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.answersubset', verbose_name='Набор ответов на секцию')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]