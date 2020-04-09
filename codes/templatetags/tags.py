from datetime import datetime
import pytz

from django import template

register = template.Library()

@register.filter
def in_the_past(value):
    now = datetime.now(pytz.utc)
    print(value < now)
    return value < now


@register.filter
def in_the_future(value):
    now = datetime.now(pytz.utc)
    print(value > now)
    return value > now
