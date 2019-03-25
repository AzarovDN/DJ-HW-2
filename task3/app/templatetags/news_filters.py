from django import template
from datetime import datetime


register = template.Library()


@register.filter
def format_date(value):
    now = datetime.now()
    then = datetime.fromtimestamp(value)
    delta = now - then
    seconds = delta.total_seconds()
    minutes = (seconds % 3600) // 60
    hours = seconds // 3600
    if minutes < 10:
        return "только что"
    elif hours < 24:
        return f'{int(hours)} часов назад'
    return then.strftime("%Y-%m-%d")


@register.filter
def format_score(value):
    if value < -5:
        return 'все плохо'
    elif (-5 < value) and (value <= 5):
        return 'нейтрально'
    return 'хорошо.'


@register.filter
def format_num_comments(value):
    if value == 0:
        return 'оставьте комментарий'
    elif value < 50:
        return value
    return '50+'

@register.filter
def format_selftext(value, arg):
    if value:
        start = value.split()[:arg]
        finish = value.split()[-arg:]
        result = ' '.join(start) + ' ... ' + ' '.join(finish)
        print(111, finish)
        return result
    return value

