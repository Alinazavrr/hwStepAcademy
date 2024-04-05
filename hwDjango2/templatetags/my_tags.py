from datetime import datetime

from django import template


register = template.Library()

@register.simple_tag
def length(value: str):
    return f" {value} have {len(value)} characters "


@register.simple_tag
def current_day():
    return f"current day: {datetime.now().day}/{datetime.now().month}/{datetime.now().year}"


@register.filter
def without_o(value: str):
    a = []
    for i in value:
        if i == 'o' or i == 'O':
            continue
        else:
            a.append(i)
    return ''.join(a)