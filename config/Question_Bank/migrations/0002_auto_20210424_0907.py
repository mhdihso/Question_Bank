# Generated by Django 3.1.7 on 2021-04-24 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question_Bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer_text',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='متن جواب'),
        ),
    ]
