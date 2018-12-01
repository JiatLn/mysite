from django import template
from django.utils.safestring import mark_safe

import libgravatar
 
register = template.Library()

# return an image tag with the gravatar
# TEMPLATE USE:  {{ email|gravatar }}
@register.filter
def gravatar(email):
    g = libgravatar.Gravatar(email)
    return g.get_image()
