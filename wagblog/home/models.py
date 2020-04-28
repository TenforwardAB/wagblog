from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                         StreamFieldPanel, InlinePanel)
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.blocks import RawHTMLBlock, BlockQuoteBlock, RichTextBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.blocks import StructBlock, RichTextBlock, CharBlock, StreamBlock

from wagblog.streams.blocks import RowBlock, WagQuoteBlock, TwoColumnBlock, FourColumnBlock


class HomePageCarouselImages(Orderable):
    """Between 1 and 5 Images for the top Banner block för the home page"""

    page = ParentalKey('home.HomePage', related_name='carousel_images')
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [ImageChooserPanel('carousel_image')]



class HomePage(Page):
    content = StreamField(
        [
            ('Image', ImageChooserBlock()),
            ('raw_html', RawHTMLBlock()),
            ('paragraph', RichTextBlock()),
            ('block_quote', WagQuoteBlock()),
            ('two_column_block', TwoColumnBlock()),
            ('four_column_block', FourColumnBlock()),
        ],
        blank=True,
        null=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel('carousel_images', max_num=5, min_num=1, label='Image'),
        ],
            heading='Carousel Image',
        ),
        StreamFieldPanel('content'),
    ]

    class Meta:  # noqa

        verbose_name = 'Home Page'
