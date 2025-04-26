from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    menu_items = MenuItem.objects.filter(
        menu_name=menu_name
    ).select_related('parent')

    menu_dict = {}
    for item in menu_items:
        menu_dict[item.id] = {
            'item': item,
            'children': [],
            'parent_id': item.parent_id,
        }

    root_items = []
    for item in menu_items:
        if item.parent_id:
            menu_dict[item.parent_id]['children'].append(menu_dict[item.id])
        else:
            root_items.append(menu_dict[item.id])

    active_item = None
    for item in menu_items:
        if item.get_absolute_url() == current_path:
            active_item = item
            break

    active_branch = set()
    current = active_item
    while current:
        active_branch.add(current.id)
        current = current.parent

    return {
        'menu_items': root_items,
        'active_branch': active_branch,
        'current_path': current_path
    }
