# Generated by Django 2.1.7 on 2019-03-14 15:23

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190314_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='news',
            field=wagtail.core.fields.StreamField([('news', wagtail.core.blocks.StructBlock([('news', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('content', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('author', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('date', wagtail.core.blocks.DateBlock(required=True))])))]))], blank=True),
        ),
    ]
