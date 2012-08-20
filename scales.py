
from intervals import Intervals

# read intervals out for reference
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

class Scale(object):
   '''Defines a collection of intervals'''

   def __init__(self, n, inters):
      '''Creates a scale instance'''
      self.name = n
      self.intervals = inters

   def voice(self, key):
      '''Voices this scale in a particular key'''
      pass

   def make_mode(self, n, mode):
      '''Re-arranges the intervals of this scale into a new scale'''

      # get the key distance to adjust all others by
      key_dist = self.intervals[mode - 1].distance
      adj_dist = []

      # build a list of distances
      for i in range(len(self.intervals)):
         # find the interval index for this iteration with
         # respect to the requested mode
         step_idx = (i + (mode - 1)) % len(self.intervals)

         # pull out the distance for the interval and adjust
         # it by the distance of the mother-key's step
         step_dist = self.intervals[step_idx].distance - key_dist

         # constrain the distance to within the chromatic scale
         if step_dist < 0:
            step_dist += 12

         # get the interval and add it to the list
         adj_dist.append(Intervals.by_distance(step_dist))

      # create the scale and send it out
      return Scale(n, adj_dist)

   def __str__(self):
      '''Retruns a string representing this scale'''
      names = [i.short_name for i in self.intervals]
      return self.name + ': ' + ','.join(names)

# build basic building-block scales that all other modes
# will be built from
major_scale  = Scale('Ionian',         [peru, maj2, maj3, per4, per5, maj6, maj7])
hminor_scale = Scale('Harmonic Minor', [peru, maj2, min3, per4, per5, min6, maj7])
mminor_scale = Scale('Melodic Minor',  [peru, maj2, min3, per4, per5, maj6, maj7])

class Scales(object):
   '''Defines a collection of scales'''

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
      hminor_scale.make_mode('Super Locrian', 7),

      mminor_scale,
      mminor_scale.make_mode('Dorian b2', 2),
      mminor_scale.make_mode('Lydian #5', 3),
      mminor_scale.make_mode('Lydian Dominant', 4),
      mminor_scale.make_mode('Mixolydian b6', 5),
      mminor_scale.make_mode('Aeolian b5', 6),
      mminor_scale.make_mode('Altered Scale', 7)
   ]


