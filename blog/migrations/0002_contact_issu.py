# Generated by Django 3.1.7 on 2021-03-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='issu',
            field=models.CharField(default='a', max_length=300),
        ),
    ]
