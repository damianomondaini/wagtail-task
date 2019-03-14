# Generated by Django 2.1.7 on 2019-03-12 13:10

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190312_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='client',
            field=wagtail.core.fields.StreamField([('client', wagtail.core.blocks.StreamBlock([('client', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('project', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('testimonial', wagtail.core.blocks.CharBlock(max_length=350, required=True)), ('client', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('quote', wagtail.images.blocks.ImageChooserBlock(required=True)), ('logo1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('logo2', wagtail.images.blocks.ImageChooserBlock(required=True)), ('logo3', wagtail.images.blocks.ImageChooserBlock(required=True)), ('logo4', wagtail.images.blocks.ImageChooserBlock(required=True)), ('logo5', wagtail.images.blocks.ImageChooserBlock(required=True)), ('logo6', wagtail.images.blocks.ImageChooserBlock(required=True))])))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='project',
            field=wagtail.core.fields.StreamField([('project', wagtail.core.blocks.StructBlock([('project', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('client', wagtail.core.blocks.CharBlock(max_length=30, required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=True))])))]))], blank=True),
        ),
    ]