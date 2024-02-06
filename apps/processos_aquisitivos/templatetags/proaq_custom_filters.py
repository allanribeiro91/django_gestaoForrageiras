from django import template

register = template.Library()

@register.filter
def get_dynamic_field(value, arg):
    """Tenta obter um campo dinâmico de um objeto."""
    print(f"Getting dynamic field: f{arg}_status")  # Adicione esta linha
    try:
        return getattr(value, f"f{arg}_status")
    except AttributeError:
        print(f"AttributeError for: f{arg}_status")  # E esta
        return None


@register.filter
def get_form_field(form, field_name):
    """Tenta obter um campo de um formulário."""
    try:
        return form[field_name]
    except KeyError:
        return None


@register.simple_tag
def get_form_field_value(form, base_name, number, suffix):
    """Tenta obter um valor de um campo de um formulário."""
    field_name = f"{base_name}{number}{suffix}"
    try:
        return form[field_name].value()
    except KeyError:
        return None



@register.filter(name='get_item')
def get_item(list, index):
    try:
        return list[index]
    except IndexError:
        return None


