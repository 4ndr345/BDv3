#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =============================================================================
# BladeDesigner
# Copyright (C) 2014 Andreas Kührmann [andreas.kuehrmann@gmail.com]

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
# =============================================================================


import numpy as np

from .. import distribution


class Joukowski(object):

    def __init__(self, max_camber):
        self.max_camber = max_camber
        self.resolution = 200
        self.distribution = distribution.Chebyshev()

    @property
    def derivatives(self):
        x = self.distribution(self.resolution)
        return self.max_camber * (1 - 2 * x)

    def as_array(self):
        x = self.distribution(self.resolution)
        y = self.max_camber * x * (1 - x)
        return np.reshape(np.append(x, y), (-1, 2), 'F')
