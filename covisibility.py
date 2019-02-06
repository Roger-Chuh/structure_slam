from threading import Lock

from collections import defaultdict, Counter
from itertools import chain


class CovisibilityGraph(object):
    def __init__(self, ):
        self.kfs = []
        self.pts = set()
        
        self.kfs_set = set()
        self.meas_lookup = dict()

    def keyframes(self):
        return self.kfs.copy()

    def mappoints(self):
        return self.pts.copy()

    def add_keyframe(self, kf):
        self.kfs.append(kf)
        self.kfs_set.add(kf)

    def add_mappoint(self, pt):
        self.pts.add(pt)

    def add_measurement(self, kf, pt, meas):
        if kf not in self.kfs_set or pt not in self.pts:
            return

        meas.keyframe = kf
        meas.mappoint = pt
        kf.add_measurement(meas)
        pt.add_measurement(meas)

        self.meas_lookup[meas.id] = meas
