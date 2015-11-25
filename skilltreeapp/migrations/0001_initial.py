# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Completed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_completed', models.DateField()),
                ('date_verified', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LearningConcept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('category', models.ForeignKey(to='skilltreeapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Prerequisite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_concept', models.ForeignKey(related_name='from_concept', to='skilltreeapp.LearningConcept')),
                ('to_concept', models.ManyToManyField(related_name='to_concept', to='skilltreeapp.LearningConcept')),
            ],
        ),
        migrations.AddField(
            model_name='learningconcept',
            name='prerequisite',
            field=models.ManyToManyField(to='skilltreeapp.LearningConcept', through='skilltreeapp.Prerequisite'),
        ),
        migrations.AddField(
            model_name='completed',
            name='concept',
            field=models.OneToOneField(to='skilltreeapp.LearningConcept'),
        ),
        migrations.AddField(
            model_name='completed',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
