# Generated by Django 3.1.7 on 2021-03-28 07:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option1', models.CharField(max_length=150)),
                ('option2', models.CharField(max_length=150)),
                ('option3', models.CharField(max_length=150)),
                ('option4', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Fileds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_qu', models.TextField(choices=[('1', 'Four options'), ('2', 'Descriptive '), ('3', 'True or False'), ('4', 'blank')], max_length=1)),
                ('text', models.CharField(max_length=250)),
                ('answer', models.CharField(max_length=150)),
                ('question_image', models.ImageField(blank=True, null=True, upload_to='Questions_img')),
                ('answer_image', models.ImageField(blank=True, null=True, upload_to='Answer_img')),
                ('hardness', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('source', models.CharField(max_length=100)),
                ('choices', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Question_Bank.choises')),
                ('lesson', models.ManyToManyField(to='Question_Bank.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Periods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fileds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question_Bank.fileds')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question_Bank.periods'),
        ),
        migrations.AddField(
            model_name='fileds',
            name='grades',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Question_Bank.grades'),
        ),
    ]
