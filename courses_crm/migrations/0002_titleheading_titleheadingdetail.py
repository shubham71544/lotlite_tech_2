# Generated by Django 5.0.6 on 2024-07-15 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitleHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='title_headings', to='courses_crm.course')),
            ],
        ),
        migrations.CreateModel(
            name='TitleHeadingDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('title_heading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='courses_crm.titleheading')),
            ],
        ),
    ]
