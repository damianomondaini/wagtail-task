# Generated by Django 2.1.7 on 2019-03-12 11:04

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190312_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='project1_client',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='project1_image',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='project1_link',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='project2_client',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='project2_image',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='project2_link',
        ),
        migrations.AddField(
            model_name='homepage',
            name='project',
            field=wagtail.core.fields.StreamField([], blank=True),
        ),
    ]
