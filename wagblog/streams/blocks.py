from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.core.blocks import StructBlock, RichTextBlock, CharBlock, StreamBlock, ChoiceBlock, ListBlock
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

from django import forms
from django.apps import apps
from django.contrib.staticfiles.templatetags.staticfiles import static


COLOUR_CHOICES = [
    ('orange-full', 'orange'),
    ('shared-section', 'green')
]


class RowBlock(StructBlock):
    paragraph = RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        icon = "edit"
        label = "Paragraph with Image"


class WagQuoteBlock(StructBlock):
    quote = CharBlock(help_text='The Text to be Quoted')
    author = CharBlock(help_text='Source of quote')

    class Meta:
        template = 'wag_quote.html'
        icon = 'openquote'
        label = ' Quote for WagBlog'


class TwoColumnBlock(StructBlock):
    background = ChoiceBlock(choices=COLOUR_CHOICES, default="orange")
    left_column = StreamBlock([
        ('heading', CharBlock(classname="full title")),
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
    ], icon='arrow-left', label='Left column content')

    right_column = StreamBlock([
        ('heading', CharBlock(classname="full title")),
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
    ], icon='arrow-right', label='Right column content')

    class Meta:
        template = 'blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class FourColumnBlock(StructBlock):
    """4 column block for price/service etc"""
    background = ChoiceBlock(choices=COLOUR_CHOICES, default="orange")
    block_title = CharBlock(classname='block title')
    block_subtitle = CharBlock(classname='block subtitle')

    first_column = StructBlock([
        ('heading', CharBlock(classname="description")),
        ('subheading', CharBlock(classname="sub description")),
        ('bigtext', CharBlock(classname="bigtext")),
        ('toplist', ListBlock(
            CharBlock(classname='top list')
        )),
        ('bottomlist', ListBlock(
            CharBlock(classname='bottom list')
        )),
    ])

    second_column = StructBlock([
        ('heading', CharBlock(classname="description")),
        ('subheading', CharBlock(classname="sub description")),
        ('bigtext', CharBlock(classname="bigtext")),
        ('toplist', ListBlock(
            CharBlock(classname='top list')
        )),
        ('bottomlist', ListBlock(
            CharBlock(classname='bottom list')
        )),
    ])

    third_column = StructBlock([
        ('heading', CharBlock(classname="description")),
        ('subheading', CharBlock(classname="sub description")),
        ('bigtext', CharBlock(classname="bigtext")),
        ('toplist', ListBlock(
            CharBlock(classname='top list')
        )),
        ('bottomlist', ListBlock(
            CharBlock(classname='bottom list')
        )),
    ])

    fourth_column = StructBlock([
        ('heading', CharBlock(classname="description")),
        ('subheading', CharBlock(classname="sub description")),
        ('bigtext', CharBlock(classname="bigtext")),
        ('toplist', ListBlock(
            CharBlock(classname='top list')
        )),  #Max number is 3
        ('bottomlist', ListBlock(
            CharBlock(classname='bottom list')
        )),
    ])

    class Meta:
        template = 'blocks/four_column_block.html'
        icon = 'placeholder'
        label = 'Four Columns'
