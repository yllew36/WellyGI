# Generated by Django 2.2.1 on 2019-08-29 03:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190829_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alamat',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='waktu_posting',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
