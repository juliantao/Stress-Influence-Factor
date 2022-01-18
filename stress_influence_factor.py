#!/usr/bin/env python
# coding: utf-8

# This script presents the common calculation methods for stress increment induced by a rectangular loading.
#
# Defination of the problem:
#
# Known:
# 1) the loading is uniformly applied on an area measures B (width) x L (Length) at the ground surface
#
# 2) Point A is located below the center of the area at a depth of zf
#
# 3) Point B is located below the corner of the area at a depth of zf
#
# Solve:
# 1) the stress influence factor at A using a) Boussinesq method (Newark's solution); b) Poulos approximation method; c) 1:2 method
#
# 2) the stress influence factor at B using a) Boussinesq method (Newark's solution); b) 1:2 method
#
# To Use the Code:
# 1) update the geometry parameters B, L and zf
#
# 2) hit run button and review the results
#


import math

#### function I_B defines the Newark's solution for Boussinesq method and calculate the influence factor IB under the corner of a rectangle loading area


def I_B(B, L, zf):
    # first term
    t1 = B ** 2 + L ** 2 + zf ** 2
    # second term
    t2 = B ** 2 * L ** 2
    # third term
    t3 = zf ** 2
    # first ratio
    r1 = 2 * B * L * zf * math.sqrt(t1) / (t3 * t1 + t2)
    # second ratio
    r2 = (t1 + zf * zf) / t1

    if t1 < t2 / t3:

        I_b = 1 / 4 / math.pi * (r1 * r2 + math.pi - math.asin(r1))

    else:

        I_b = 1 / 4 / math.pi * (r1 * r2 + math.asin(r1))

        return I_b


#### function I_Poulos defines Poulus approximation equation to calculate the influence factor IB under the center of a rectangle loading area
def I_Poulos(B, L, zf):

    I_Poulos = 1 - (1 / (1 + (B / 2 / zf) ** (1.38 + 0.62 * B / L))) ** (
        2.60 - 0.84 * B / L
    )
    return I_Poulos


#### function I_12 defines the 1:2 method to calculate the influence factor IB
def I_12(B, L, zf):

    I_12 = (B * L) / (B + zf) / (L + zf)
    return I_12


#############################################
###############Input###############
#############################################
B = 0.5
L = 1.0
zf = 1.2

IB_corner = I_B(B, L, zf)
IB_center = 4 * I_B(B / 2, L / 2, zf)
I_Poulos = I_Poulos(B, L, zf)
I12 = I_12(B, L, zf)

delta_BP = (I_Poulos - IB_center) / IB_center
delta_B12 = (I12 - IB_center) / IB_center
delta_P12 = (I_Poulos - I12) / I_Poulos

print(
    "Under the corner, the  stress influence factor calculated using the Boussinesq method is: ",
    IB_corner,
)
print(
    "Under the center, the stress influence factor calculated using the Boussinesq method is: ",
    IB_center,
)
print(
    "Under the center, the stress influence factor calculated using the Poulus approximation method is: ",
    I_Poulos,
)
print(
    "Under the center, the  stress influence factor calculated using the 1:2 method is: ",
    I12,
)

print(
    "The difference percentages, delta_BP, delta_B12 and delta_P12 are ",
    delta_BP,
    delta_B12,
    delta_P12,
)
