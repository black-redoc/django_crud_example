from django import template

register = template.Library()

@register.filter
def cut_text(value):
    """ returns a cut string if its length is greater than 50 chars """
    return value if len(value) <= 50 else f"{value[:50]}..."