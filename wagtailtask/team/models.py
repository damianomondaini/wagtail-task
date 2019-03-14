from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from streams import blocks

class TeamPage(Page):
    template = "team/team_page.html"
    max_count = 1

    team = StreamField(
        [
            ("service", blocks.TeamBlock())
        ],
        null=False,
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("team"),
    ]
