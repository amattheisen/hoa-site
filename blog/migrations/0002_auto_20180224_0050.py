# Generated by Django 2.0.2 on 2018-02-24 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(max_length=2500),
        ),
    ]
