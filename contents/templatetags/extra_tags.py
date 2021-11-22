from django import template
register = template.Library()

@register.filter(name='addcss_item_create')
def addcss_item_create(field, css):
    return field.as_widget(attrs={"class":css})