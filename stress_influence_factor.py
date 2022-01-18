#!/usr/bin/env python
# coding: utf-8

# This notebook presents the common calculation methods for stress increment induced by a rectangular loading.
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

#### function IB defines the Newark's solution for Boussinesq method and calculate the influence factor IB under the corner of a rectangle loading area


def IB(B, L, zf):

    if B ** 2 + L ** 2 + zf ** 2 < B ** 2 * L ** 2 / zf ** 2:
        I = (
            1
            / 4
            / math.pi
            * (
                (
                    2
                    * B
                    * L
                    * zf
                    * (B ** 2 + L ** 2 + zf ** 2) ** 0.5
                    / (zf ** 2 * (B ** 2 + L ** 2 + zf ** 2) + B ** 2 * L ** 2)
                )
                * ((B ** 2 + L ** 2 + 2 * zf ** 2) / (B ** 2 + L ** 2 + zf ** 2))
                + math.pi
                - math.asin(
                    2
                    * B
                    * L
                    * zf
                    * (B ** 2 + L ** 2 + zf ** 2) ** 0.5
                    / (zf ** 2 * (B ** 2 + L ** 2 + zf ** 2) + B ** 2 * L ** 2)
                )
            )
        )
    else:
        I = (
            1
            / 4
            / math.pi
            * (
                (
                    2
                    * B
                    * L
                    * zf
                    * (B ** 2 + L ** 2 + zf ** 2) ** 0.5
                    / (zf ** 2 * (B ** 2 + L ** 2 + zf ** 2) + B ** 2 * L ** 2)
                )
                * ((B ** 2 + L ** 2 + 2 * zf ** 2) / (B ** 2 + L ** 2 + zf ** 2))
                + math.asin(
                    2
                    * B
                    * L
                    * zf
                    * (B ** 2 + L ** 2 + zf ** 2) ** 0.5
                    / (zf ** 2 * (B ** 2 + L ** 2 + zf ** 2) + B ** 2 * L ** 2)
                )
            )
        )
        return I


#### function I_Poulos defines Poulus approximation equation to calculate the influence factor IB under the center of a rectangle loading area
def I_Poulos(B, L, zf):

    I_Poulos = 1 - (1 / (1 + (B / 2 / zf) ** (1.38 + 0.62 * B / L))) ** (
        2.60 - 0.84 * B / L
    )
    return I_Poulos


#### function I12 defines the 1:2 method to calculate the influence factor IB
def I12(B, L, zf):

    I12 = (B * L) / (B + zf) / (L + zf)
    return I12


# In[ ]:

## input
B = 0.5
L = 1.0
zf = 1.2


IB_corner = IB(B, L, zf)
I12 = I12(B, L, zf)
IB_center = 4 * IB(B / 2, L / 2, zf)
I_Poulos = I_Poulos(B, L, zf)


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
    "Under the corner, the  stress influence factor calculated using the Boussinesq method is: ",
    IB_corner,
)


# In[ ]:
