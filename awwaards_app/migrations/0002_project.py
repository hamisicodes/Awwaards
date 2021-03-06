# Generated by Django 3.0.7 on 2020-06-08 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awwaards_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='projects/')),
                ('publish_at', models.DateTimeField(auto_now_add=True)),
                ('link', models.URLField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awwaards_app.Profile')),
            ],
            options={
                'ordering': ['-publish_at'],
            },
        ),
    ]
