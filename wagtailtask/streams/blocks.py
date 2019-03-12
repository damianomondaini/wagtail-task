from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.blocks import PageChooserBlock

class TextBlock(blocks.StructBlock):
    text = blocks.TextBlock(required=True, help_text="Add text")

    class Meta:
        template = "streams/text_block.html"
        icon = "edit"
        label = "Text"

class ServiceBlock(blocks.StructBlock):
    service = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", DocumentChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=30)),
                ("description", blocks.CharBlock(required=True)),
                ("blob", DocumentChooserBlock(required=True)),
            ]
        )
    )

    class Meta:
        template = "streams/service_block.html"
        icon = "form"
        label = "Service"

class ProjectBlock(blocks.StructBlock):
    project = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("client", blocks.CharBlock(required=True, max_length=30)),
                ("link", PageChooserBlock(required=True)),
            ]
        )
    )

    class Meta:
        template = "streams/project_block.html"
        icon = "folder"
        label = "Project"

class ClientBlock(blocks.StructBlock):
    client = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("project", blocks.CharBlock(required=True, max_length=50)),
                ("testimonial", blocks.CharBlock(required=True, max_length=350)),
                ("client", blocks.CharBlock(required=True, max_length=50)),
                ("quote", DocumentChooserBlock(required=True)),
                ("logo1", ImageChooserBlock(required=True)),
                ("logo2", ImageChooserBlock(required=True)),
                ("logo3", ImageChooserBlock(required=True)),
                ("logo4", ImageChooserBlock(required=True)),
                ("logo5", ImageChooserBlock(required=True)),
                ("logo6", ImageChooserBlock(required=True)),
            ]
        )
    )

    class Meta:
        template = "streams/client_block.html"
        icon = "user"
        label = "Client"