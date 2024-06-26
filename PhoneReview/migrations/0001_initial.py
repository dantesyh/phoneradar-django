# Generated by Django 4.2.1 on 2023-05-06 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('origin', models.CharField(max_length=20)),
                ('manufacturing_since', models.IntegerField()),
                ('slug', models.SlugField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('launch_date', models.DateField()),
                ('platform', models.CharField(max_length=20)),
                ('slug', models.SlugField(default='', max_length=150)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PhoneReview.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('date', models.DateField()),
                ('slug', models.SlugField(default='', max_length=150)),
                ('model', models.ManyToManyField(to='PhoneReview.model')),
            ],
        ),
    ]
