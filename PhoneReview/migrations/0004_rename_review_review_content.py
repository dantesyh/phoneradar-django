# Generated by Django 4.2.1 on 2023-05-06 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PhoneReview', '0003_review_news_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='content',
        ),
    ]
