# Generated by Django 4.2.1 on 2023-05-06 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhoneReview', '0002_review_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='news_link',
            field=models.TextField(blank=True),
        ),
    ]