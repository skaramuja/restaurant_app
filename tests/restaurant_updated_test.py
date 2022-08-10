import unittest

from model.restaurant_updater import RestaurantUpdater


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.restaurant_updater = RestaurantUpdater('McDonalds', '1807 Elm Street', 'West Des Moines', 'Iowa', "50265", "1")

    def tearDown(self):
        del self.restaurant_updater

    # constructor with invalid name
    def test_object_created_with_invalid_name(self):
        with self.assertRaises(ValueError):
            p = RestaurantUpdater('', '1807 Elm Street', 'West Des Moines', 'Iowa', "50265", "1")

    # constructor with invalid street
    def test_object_created_with_invalid_street(self):
        with self.assertRaises(ValueError):
            p = RestaurantUpdater('McDonalds', '', 'West Des Moines', 'Iowa', "50265", "1")

    # constructor with invalid city
    def test_object_created_with_invalid_city(self):
        with self.assertRaises(ValueError):
            p = RestaurantUpdater('McDonalds', '1807 Elm Street', '', 'Iowa', "50265", "1")

    # constructor with invalid state
    def test_object_created_with_invalid_state(self):
        with self.assertRaises(ValueError):
            p = RestaurantUpdater('McDonalds', '1807 Elm Street', 'West Des Moines', '', "50265", "1")

    # constructor with invalid zipcode
    def test_object_created_with_invalid_zip_code(self):
        with self.assertRaises(ValueError):
            p = RestaurantUpdater('McDonalds', '1807 Elm Street', 'West Des Moines', 'Iowa', "", "1")

    # constructor with invalid zipcode value type
    def test_object_created_with_invalid_zip_code_two(self):
        with self.assertRaises(ValueError):
            p = RestaurantUpdater('McDonalds', '1807 Elm Street', 'West Des Moines', 'Iowa', "ABC", "1")

    # constructor with invalid rating blank
    def test_object_created_with_invalid_rating(self):
        with self.assertRaises(ValueError):
            p = RestaurantUpdater('McDonalds', '1807 Elm Street', 'West Des Moines', 'Iowa', "50265", "")

    # constructor with invalid rating range
    def test_object_created_with_invalid_rating_two(self):
        with self.assertRaises(ValueError):
            p = RestaurantUpdater('McDonalds', '1807 Elm Street', 'West Des Moines', 'Iowa', "50265", "15")

     # constructor with invalid rating range
    def test_object_created_with_invalid_rating_three(self):
        with self.assertRaises(ValueError):
            p = RestaurantUpdater('McDonalds', '1807 Elm Street', 'West Des Moines', 'Iowa', "50265", "0")

      # constructor with invalid rating value type
    def test_object_created_with_invalid_rating_four(self):
        with self.assertRaises(ValueError):
            p = RestaurantUpdater('McDonalds', '1807 Elm Street', 'West Des Moines', 'Iowa', "50265", "ABC")


if __name__ == '__main__':
    unittest.main()
