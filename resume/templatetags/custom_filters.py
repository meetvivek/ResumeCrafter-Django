# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def split(value, arg):
    return value.split(arg)

@register.filter
def trim(value):
    return value.strip() if isinstance(value, str) else value

@register.filter
def split_newline(value):
    """Splits the text by newline characters and returns a list"""
    return value.split('\n')