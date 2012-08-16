
from symbols import Symbols

class Note(object):
   '''Represents a note within the chromatic scale'''

   def __init__(self, sname, fname, dist):
      '''Initialize this note object'''
      self.flat_name = fname
      self.sharp_name = sname
      self.distance = dist

   def is_natural(self):
      '''Determines if this note is natural or not'''
      return self.flat_name == self.sharp_name

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
      '''Returns a string representing this note'''
      if self.flat_name == self.sharp_name:
         return self.flat_name
      else:
         return self.flat_name + Symbols.FLAT  + '/' + self.sharp_name + Symbols.SHARP

class Notes(object):
   '''Provides intelligent list access to the chromatic scale'''

   chromatic_scale = [
         Note('c', 'c', 0),
         Note('c', 'd', 1),
         Note('d', 'd', 2),
         Note('d', 'e', 3),
         Note('e', 'e', 4),
         Note('f', 'f', 5),
         Note('f', 'g', 6),
         Note('g', 'g', 7),
         Note('g', 'a', 8),
         Note('a', 'a', 9),
         Note('a', 'b', 10),
         Note('b', 'b', 11)
         ]

   @staticmethod
   def by_distance(dist):
      '''Finds a note object by distance'''
      return [n for n in Notes.chromatic_scale if n.distance == dist][0]


