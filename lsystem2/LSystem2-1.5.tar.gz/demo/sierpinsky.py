#!/usr/bin/env python
import LSystem2

__revision__ = "$Id: sierpinsky.py 71 2005-12-04 20:08:21Z const $"

D = 128

L = LSystem2.LSystem()
L.production = (4, 0), (-1, 3**0.5), (-1, -3**0.5), (2, 0)
L.state = (2 * D, 0), (-D, D * 3**0.5), (-D, -D * 3**0.5)
L.depth = 6

eps = LSystem2.EPS(title = "Sierpinsky's Tetrahedron")
eps.stroke(L, setlinewidth = 0.4, setrgbcolor = (0.4, 0.2, 0.6))
eps.write(file("sierpinsky.eps", "w"))
