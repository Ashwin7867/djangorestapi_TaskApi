# Generated by Django 3.0.5 on 2020-04-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='doc',
            field=models.FileField(default='Doc/None/No-doc.pdf', upload_to='Doc/'),
        ),
    ]