# Generated by Django 3.1.1 on 2021-04-16 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210416_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='benefits',
            field=models.TextField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='application',
            name='notes',
            field=models.TextField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='application',
            name='pay',
            field=models.CharField(default='N/A', max_length=30),
        ),
    ]