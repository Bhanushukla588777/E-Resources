# Generated by Django 4.0.4 on 2022-06-06 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MixDoc', '0015_resume_projects_resume_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='intro',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
