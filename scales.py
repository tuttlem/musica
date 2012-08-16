
from intervals import Intervals

class Scale(object):
   '''Defines a collection of intervals'''

   def __init__(self, n, inters):
      '''Creates a scale instance'''
      self.name = n
      self.intervals = n

   def voice(self, key):
      '''Voices this scale in a particular key'''
      pass

   def make_mode(self, n, mode):
      '''Re-arranges the intervals of this scale into a new scale'''
      pass

class Scales(object):
   '''Defines a collection of scales'''

peru = Intervals.by_distance(0)
min2 = Intervals.by_distance(1)
maj2 = Intervals.by_distance(2)
min3 = Intervals.by_distance(3)
maj3 = Intervals.by_distance(4)
per4 = Intervals.by_distance(5)
trit = Intervals.by_distance(6)
per5 = Intervals.by_distance(7)
min6 = Intervals.by_distance(8)
maj6 = Intervals.by_distance(9)
min7 = Intervals.by_distance(10)
maj7 = Intervals.by_distance(11)

major_scale  = Scale('Ionian', [peru, maj2, maj3, per4, per5, maj6, maj7])
hminor_scale = Scale('Harmonic Minor', [peru, maj2, min3, per4, per5, min6, maj7])

scales = [
   major_scale,
   major_scale.make_mode('Dorian', 2),
   major_scale.make_mode('Phrygian', 3),
   major_scale.make_mode('Lydian', 4),
   major_scale.make_mode('Mixolydian', 5),
   major_scale.make_mode('Aeolian', 6),
   major_scale.make_mode('Locrian', 7),

   hminor_scale,
   hminor_scale.make_mode('Locrian #6', 2),
   hminor_scale.make_mode('Ionian #5', 3),
   hminor_scale.make_mode('Dorian #4', 4),
   hminor_scale.make_mode('Phrygian Dominant', 5),
   hminor_scale.make_mode('Lydian #2', 6),
   hminor_scale.make_mode('Super Locrian', 7)
]
