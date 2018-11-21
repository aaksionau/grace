from django import template

register = template.Library()

@register.filter
def doublequote_quote(value):
    return str(value).replace('"','\'')
