import unittest
import telephones


class TestTelephoneType(unittest.TestCase):
    def test_telemarketers(self):
        result = telephones.get_telephone_type('1408371942')

        self.assertEqual('telemarketers', result)

    def test_fixed(self):
        result = telephones.get_telephone_type('(080)43215621')
        self.assertEqual('fixed', result)

    def test_mobile(self):
        result = telephones.get_telephone_type('94489 72078')
        self.assertEqual('mobile', result)


class TestFixedLocation(unittest.TestCase):
    def test_bangalore(self):
        result = telephones.get_fixed_location('(080)43215621')
        self.assertEqual('Bangalore', result)

    def test_unknown(self):
        result = telephones.get_fixed_location('(0471)2953539')
        self.assertEqual('Unknown', result)


class TestCodeType(unittest.TestCase):
    def test_telemarketers(self):
        result = telephones.get_area_code('1408371942')
        self.assertEqual('140', result)

    def test_fixed(self):
        result = telephones.get_area_code('(08888)12345678')
        self.assertEqual('(08888)', result)

    def test_mobile(self):
        result = telephones.get_area_code('94489 7229')
        self.assertEqual('94489', result)


if __name__ == '__main__':
    unittest.main()
