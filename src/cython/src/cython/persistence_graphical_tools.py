import matplotlib.pyplot as plt
import numpy as np

"""This file is part of the Gudhi Library. The Gudhi library
   (Geometric Understanding in Higher Dimensions) is a generic C++
   library for computational topology.

   Author(s):       Vincent Rouvreau

   Copyright (C) 2016 INRIA

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Vincent Rouvreau"
__copyright__ = "Copyright (C) 2016 INRIA"
__license__ = "GPL v3"

"""
Only 13 colors for the palette
"""
palette = ['#ff0000', '#00ff00', '#0000ff', '#00ffff', '#ff00ff', '#ffff00',
           '#000000', '#880000', '#008800', '#000088', '#888800', '#880088',
           '#008888']

def show_palette_values():
    colors = []
    for color in palette:
        colors.append(color)

    y_pos = np.arange(len(palette))

    plt.barh(y_pos, y_pos + 1, align='center', alpha=0.4, color=colors)
    plt.ylabel('Dimension')
    plt.title('Dimension palette values')

    plt.show()

def bar_code_persistence(persistence):
    # Look for minimum birth date and maximum death date for plot optimisation
    max_death = 0
    min_birth = persistence[0][1][0]
    for interval in reversed(persistence):
        if float(interval[1][1]) != float('inf'):
            if float(interval[1][1]) > max_death:
                max_death = float(interval[1][1])
        if float(interval[1][0]) > max_death:
            max_death = float(interval[1][0])
        if float(interval[1][0]) < min_birth:
            min_birth = float(interval[1][0])

    ind = 0
    delta = ((max_death - min_birth) / 10.0)
    infinity = max_death + delta
    axis_start = min_birth - delta
    # Draw horizontal bars in loop
    for interval in reversed(persistence):
        if float(interval[1][1]) != float('inf'):
            # Finite death case
            plt.barh(ind, (interval[1][1] - interval[1][0]), height=0.8,
                     left = interval[1][0], alpha=0.4,
                     color = palette[interval[0]])
        else:
            # Infinite death case for diagram to be nicer
            plt.barh(ind, (infinity - interval[1][0]), height=0.8,
                     left = interval[1][0], alpha=0.4,
                     color = palette[interval[0]])
        ind = ind + 1
    # Ends plot on infinity value and starts a little bit before min_birth
    plt.axis([axis_start, infinity, 0, ind])
    plt.show()
