# Generated by Django 2.0 on 2018-11-30 07:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('message_board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254, verbose_name='邮箱'),
            preserve_default=False,
        ),
    ]
