# Generated by Django 2.2.5 on 2019-10-02 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosmed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagram',
            name='content',
            field=models.CharField(default='programming', max_length=100),
            preserve_default=False,
        ),
    ]
