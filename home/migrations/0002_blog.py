# Generated by Django 4.2.11 on 2024-04-27 15:47

from django.db import migrations, models
import djrichtextfield.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=150)),
                ('body', djrichtextfield.models.RichTextField()),
                ('description', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='news/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
