# Generated by Django 3.1.5 on 2021-01-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210113_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.DeleteModel(
            name='PostComment',
        ),
    ]
