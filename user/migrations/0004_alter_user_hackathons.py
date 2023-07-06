# Generated by Django 4.2.3 on 2023-07-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0002_submission_submissionlinkfile_submissionimagefile_and_more'),
        ('user', '0003_alter_user_hackathons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hackathons',
            field=models.ManyToManyField(related_name='registered_hackathons', to='hackathon.hackathon'),
        ),
    ]