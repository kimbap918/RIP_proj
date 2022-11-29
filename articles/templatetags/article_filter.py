import markdown
from django import template
from django.utils.safestring import mark_safe
from atexit import register

register = template.Library()

@register.filter
def sub(value,arg):
    return value - arg