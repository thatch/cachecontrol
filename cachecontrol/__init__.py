# SPDX-FileCopyrightText: 2015 Eric Larson
#
# SPDX-License-Identifier: Apache-2.0

"""CacheControl import Interface.

Make it easy to import from cachecontrol without long namespaces.
"""
__author__ = "Eric Larson"
__email__ = "eric@ionrock.org"
__version__ = "0.13.1rc0"

from cachecontrol.adapter import CacheControlAdapter
from cachecontrol.controller import CacheController
from cachecontrol.wrapper import CacheControl

__all__ = [
    "__author__",
    "__email__",
    "__version__",
    "CacheControlAdapter",
    "CacheController",
    "CacheControl",
]

import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())
