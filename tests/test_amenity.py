import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_name_initialization(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_name_assignment(self):
        amenity = Amenity()
        amenity.name = "ALX SWE"
        self.assertEqual(amenity.name, "ALX SWE")

if __name__ == '__main__':
    unittest.main()

