# Generated by Django 2.2 on 2019-05-13 09:16

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rick', '0004_examplemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=mdeditor.fields.MDTextField(verbose_name='文章内容'),
        ),
    ]