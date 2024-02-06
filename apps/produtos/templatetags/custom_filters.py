from django import template
import locale

register = template.Library()

@register.filter
def join_tags(tags_list):
    return "; ".join(tag['tag'] for tag in tags_list)

@register.filter(name='format_number')
def format_number(value):
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.format_string("%0.2f", value, grouping=True)
    except (ValueError, TypeError):
        return value

@register.filter(name='format_percent')
def format_percent(value):
    try:
        return "{:.1%}".format(value)
    except (ValueError, TypeError):
        return ""