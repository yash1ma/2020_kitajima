# -*- coding: utf-8 -*-
# Copyright (C) 2018 by Brendt Wohlberg <brendt@ieee.org>
# All rights reserved. BSD 3-clause License.
# This file is part of the SPORCO package. Details of the copyright
# and user license can be found in the 'LICENSE.txt' file distributed
# with the package.

"""Construct variant of dictlrn subpackage that use cupy instead of numpy"""

from __future__ import absolute_import

import sys
import re

from mysporco.cupy import sporco_cupy_patch_module
from mysporco.cupy import cp
from mysporco.cupy import linalg

from mysporco.cupy import cnvrep
from mysporco.cupy.admm import cbpdn


# Construct mysporco.cupy.dictlrn
dictlrn = sporco_cupy_patch_module('mysporco.dictlrn')

# Construct mysporco.cupy.dictlrn.onlinecdl
dictlrn.onlinecdl = sporco_cupy_patch_module(
    'mysporco.dictlrn.onlinecdl', {'sl': linalg, 'cr': cnvrep, 'cbpdn': cbpdn})

# In sporco.cupy.dictlrn module, replace original module source path with
# corresponding path in 'sporco/cupy' directory tree
for n, pth in enumerate(sys.modules['mysporco.cupy.dictlrn'].__path__):
    pth = re.sub('mysporco/', 'mysporco/cupy/', pth)
    sys.modules['mysporco.cupy.dictlrn'].__path__[n] = pth