# Generated by Django 4.1 on 2023-03-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0009_alter_sivangangai_id_alter_thanjavur_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sivangangai',
            name='are',
            field=models.CharField(default='ye', max_length=2080),
        ),
        migrations.AddField(
            model_name='thanjavur',
            name='are',
            field=models.CharField(default='ye', max_length=2080),
        ),
        migrations.AddField(
            model_name='thiruvallur',
            name='are',
            field=models.CharField(default='ye', max_length=2080),
        ),
    ]
