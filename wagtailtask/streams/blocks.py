from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock

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
