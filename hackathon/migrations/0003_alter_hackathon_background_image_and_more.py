# Generated by Django 4.2.3 on 2023-07-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0002_submission_submissionlinkfile_submissionimagefile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='background_image',
            field=models.ImageField(upload_to='background_images'),
        ),
        migrations.AlterField(
            model_name='hackathon',
            name='hackathon_image',
            field=models.ImageField(upload_to='hackathon_images'),
        ),
        migrations.AlterField(
            model_name='submissionfile',
            name='file',
            field=models.FileField(upload_to='submission_files'),
        ),
        migrations.AlterField(
            model_name='submissionimagefile',
            name='image_file',
            field=models.ImageField(upload_to='submission_images'),
        ),
    ]