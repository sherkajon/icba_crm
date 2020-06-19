from .models import Menu


def navigation_bar(request):
    menu = Menu.objects.all()
    return {
        'menu_items': menu
    }
