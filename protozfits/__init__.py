from pkg_resources import resource_string
from . import digicam as do_not_use_me
from .simple import File as SimpleFile
from .any_array_to_numpy import any_array_to_numpy
from .simple import make_namedtuple

__version__ = resource_string('protozfits', 'VERSION').decode().strip()


__all__ = [
    'SimpleFile',
    'make_namedtuple',
    'any_array_to_numpy',
]
