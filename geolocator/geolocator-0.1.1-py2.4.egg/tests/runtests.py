import unittest

from geolocator.tests import LibraryTestSuite

if __name__ == "__main__":

   runner = unittest.TextTestRunner()
   runner.run(LibraryTestSuite)
