import sys
from django.template import Library
from optional_django import six
from ..compiler import webpack
from ..exceptions import BundlingError

register = Library()

@register.assignment_tag(name='webpack')
def webpack_template_tag(path_to_config):
    """
    A template tag that will output a webpack bundle.

    Usage:

        {% load webpack %}
        
        {% webpack 'path/to/webpack.config.js' %}
    """

    # TODO: allow selection of entries

    # Django's template system silently fails on some exceptions
    try:
        bundle = webpack(path_to_config)
        return bundle
    except (AttributeError, ValueError) as e:
        raise six.reraise(BundlingError, BundlingError(*e.args), sys.exc_info()[2])