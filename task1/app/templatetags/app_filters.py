from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def color_filter(col):

    if col == '':
        return mark_safe('<td> - </td>')
    elif float(col) < 0:
        color = 'bgcolor="green"'
    elif 0 <= float(col) < 1:
        color = ''
    elif 1 <= float(col) < 2:
        color = 'bgcolor=#FF8F50'
    elif 2 <= float(col) < 5:
        color = 'bgcolor=#FF8F8F'
    else:
        color = 'bgcolor=red'

    return mark_safe(f'<td {color}> {col} </td>')
