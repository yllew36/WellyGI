# Generated by Django 2.2.5 on 2019-09-26 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='author', max_length=100),
            preserve_default=False,
        ),
    ]