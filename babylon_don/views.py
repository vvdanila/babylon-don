from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def index(request):
    products = [
        {'has_preview': True, 'title': 'babylon Don Duffle Bag', 'url': '/product/babylon-don-duffle-bag'},
        {'has_preview': True, 'title': 'babylon Don Duffle Bag Reload', 'url': '/product/babylon-don-duffle-bag-reload'},
        {'has_preview': False, 'title': 'babylon Don Duffle Bag Final', 'url': '/product/babylon-don-duffle-bag-final'},
    ]
    return {'products': products}
