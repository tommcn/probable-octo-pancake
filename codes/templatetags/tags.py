from datetime import datetime
import pytz

from django import template

register = template.Library()

@register.filter
def in_the_past(value):
    """
    Is the datetime object in the past (boolean)
    """
    now = datetime.now(pytz.utc)
    print(value < now)
    return value < now


@register.filter
def in_the_future(value):
    """
    Is the datetime object in the future (boolean)
    """
    now = datetime.now(pytz.utc)
    print(value > now)
    return value > now
