# Generated by Django 4.2.1 on 2023-05-06 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhoneReview', '0004_rename_review_review_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='news_link',
        ),
        migrations.AddField(
            model_name='model',
            name='news_link',
            field=models.TextField(blank=True),
        ),
    ]