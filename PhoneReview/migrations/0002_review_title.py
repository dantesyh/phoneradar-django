# Generated by Django 4.2.1 on 2023-05-06 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhoneReview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]