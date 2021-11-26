from django import template
register = template.Library()

@register.filter(name='addcss_signup')
def addcss_signup(field, css):
    return field.as_widget(attrs={"class":css})