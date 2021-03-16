# Generated by Django 3.1.7 on 2021-03-15 16:30

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('shortcontent', models.TextField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('keyword', models.CharField(max_length=100)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=80)),
                ('image', models.ImageField(default='abc.jpg', upload_to='app/img')),
                ('authorimg', models.ImageField(default='abc.jpg', upload_to='app/authorimg')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=80)),
                ('Lastname', models.CharField(max_length=80)),
                ('Email', models.CharField(max_length=80)),
                ('Contact', models.BigIntegerField()),
                ('State', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Businessname', models.CharField(max_length=200)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=80)),
                ('Lastname', models.CharField(max_length=80)),
                ('Email', models.CharField(max_length=80)),
                ('Contact', models.BigIntegerField()),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post')),
            ],
        ),
    ]
