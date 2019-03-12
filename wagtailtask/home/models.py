from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1

    intro_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    intro_content = StreamField(
        [
            ("text_block", blocks.TextBlock())
        ],
        null=False,
        blank=True
    )
    intro_button = models.CharField(max_length=50, null=False, blank=True)

    service = StreamField(
        [
            ("service", blocks.ServiceBlock())
        ],
        null=False,
        blank=True
    )

    project = StreamField(
        [
            ("project", blocks.ProjectBlock())
        ],
        null=False,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro_button"),
        StreamFieldPanel("intro_content"),
        ImageChooserPanel("intro_image"),
        StreamFieldPanel("service"),
        StreamFieldPanel("project"),
    ]