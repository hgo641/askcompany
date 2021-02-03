# Generated by Django 3.1.5 on 2021-01-30 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_public', models.BooleanField(default=False, verbose_name='공개여부')),
                ('photo', models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')),
            ],
        ),
    ]