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


import nose.tools

from ... import camberline
from ... import distribution


def test_input_param():
    max_camber = 0.12
    cl = camberline.Joukowski(max_camber)
    nose.tools.assert_equal(cl.max_camber, 0.12)


def test_default_parameter():
    max_camber = 0.12
    cl = camberline.Joukowski(max_camber)
    nose.tools.assert_equal(cl.resolution, 200)
    nose.tools.assert_is_instance(cl.distribution, distribution.Chebyshev)


def test_start_point():
    max_camber = 0.12
    cl = camberline.Joukowski(max_camber)
    nose.tools.assert_equal(cl.as_array()[0, 1], 0)


def test_end_point():
    max_camber = 0.12
    cl = camberline.Joukowski(max_camber)
    nose.tools.assert_equal(cl.as_array()[-1, 1], 0)


def test_mid_point_with_pos_max_camber():
    max_camber = 0.12
    cl = camberline.Joukowski(max_camber)
    nose.tools.assert_greater(cl.as_array()[100, 1], 0)


def test_mid_point_with_neg_max_camber():
    max_camber = -0.12
    cl = camberline.Joukowski(max_camber)
    nose.tools.assert_less(cl.as_array()[100, 1], 0)


def test_mid_point_with_max_camber_zero():
    max_camber = 0
    cl = camberline.Joukowski(max_camber)
    nose.tools.assert_equal(cl.as_array()[100, 1], 0)


def test_start_derivative():
    max_camber = 0.12
    cl = camberline.Joukowski(max_camber)
    nose.tools.assert_greater(cl.derivatives[0], 0)


def test_end_derivative():
    max_camber = 0.12
    cl = camberline.Joukowski(max_camber)
    nose.tools.assert_less(cl.derivatives[-1], 0)
