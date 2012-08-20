
class Interval(object):
   '''Defines a single interval'''

   def __init__(self, sname, lname, dist):
      '''Creates a new interval object'''
      self.short_name = sname
      self.long_name = lname
      self.distance = dist

   def is_extended(self):
      '''Determines if this interval is outside of the first octave'''
      return self.distance > 11

   def __lt__(self, other):
      return self.distance < other.distance

   def __le__(self, other):
      return self.distance <= other.distance

   def __eq__(self, other):
      return self.distance == other.distance

   def __ne__(self, other):
      return self.distance != other.distance

   def __gt__(self, other):
      return self.distance > other.distance

   def __ge__(self, other):
      return self.distance >= other.distance

   def __unicode__(self):
      '''Returns a string representing this interval'''
      return self.short_name

   def __str__(self):
      '''Returns a string repsenting this interval'''
      return self.short_name

class Intervals(object):
   '''Defines the supported range of intervals'''

   interval_set = [
         Interval('PU',  'Perfect Unison',    0),

         Interval('m2',  'Minor Second',      1),
         Interval('M2',  'Major Second',      2),
         Interval('m3',  'Minor Third',       3),
         Interval('M3',  'Major Third',       4),
         Interval('P4',  'Perfect Fourth',    5),
         Interval('TT',  'Tritone',           6),
         Interval('P5',  'Perfect Fifth',     7),
         Interval('m6',  'Minor Sixth',       8),
         Interval('M6',  'Major Sixth',       9),
         Interval('m7',  'Minor Seventh',    10),
         Interval('M7',  'Major Seventh',    11),

         Interval('PO',  'Perfect Octave',   12),

         Interval('m9',  'Minor Ninth',      13),
         Interval('M9',  'Major Ninth',      14),
         Interval('m10', 'Minor Tenth',      15),
         Interval('M10', 'Major Tenth',      16),
         Interval('P11', 'Perfect Eleventh', 17),
         Interval('OTT', 'Octave Tritone',   18),
         Interval('P12', 'Perfect Twelth',   19),
         Interval('m13', 'Minor Thirteenth', 20),
         Interval('M13', 'Major Thirteenth', 21),
         Interval('m14', 'Minor Fourteenth', 22),
         Interval('M14', 'Major Fourteenth', 23)
   ]

   @staticmethod
   def by_distance(dist):
      '''Finds a note object by distance'''
      return [i for i in Intervals.interval_set if i.distance == dist][0]


