# Generated by Django 3.1.3 on 2021-01-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddituser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reddituser',
            name='bio',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
