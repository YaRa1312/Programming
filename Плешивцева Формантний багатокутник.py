import math
import matplotlib.patches as patches
import pylab
pp=[(747, 1394), (592, 1963), (599, 1384), (396, 1801), (373, 2090), (388, 2033)]
# compute centroid
cent=(sum([p[0] for p in pp])/len(pp),sum([p[1] for p in pp])/len(pp))
# sort by polar angle
pp.sort(key=lambda p: math.atan2(p[1]-cent[1],p[0]-cent[0]))
# plot points
pylab.scatter([p[0] for p in pp],[p[1] for p in pp])
# plot polyline
pylab.gca().add_patch(patches.Polygon(pp,closed=True,fill=False))
pylab.grid()
pylab.show()
