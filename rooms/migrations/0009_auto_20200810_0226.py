# Generated by Django 2.2.5 on 2020-08-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20200804_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.IntegerField(help_text='How many people will be staying?'),
        ),
    ]