import unittest
import telephones


class TestTelephoneType(unittest.TestCase):
    def test_telemarketers(self):
        result = telephones.get_telephone_type('1408371942')

        self.assertEqual('telemarketers', result)

    def test_fixed(self):
        result = telephones.get_telephone_type('(080)43215621')
        self.assertEqual('fixed', result)

    def test_wrong_fixed(self):
        result = telephones.get_telephone_type('(123)45678')
        self.assertEqual('unknown', result)

    def test_mobile_starting7(self):
        result = telephones.get_telephone_type('74489 72078')
        self.assertEqual('mobile', result)

    def test_mobile_starting8(self):
        result = telephones.get_telephone_type('84489 72078')
        self.assertEqual('mobile', result)

    def test_mobile_starting9(self):
        result = telephones.get_telephone_type('94489 72078')
        self.assertEqual('mobile', result)

    def test_wrong_mobile(self):
        result = telephones.get_telephone_type('12345 67899')
        self.assertEqual('unknown', result)


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
        self.assertEqual('9448', result)


class TestExtractDurations(unittest.TestCase):
    def test_longest_duration_from_multiple_calls(self):
        phone_calls = {}
        calls = [
            ['(080)40395498', '98453 94494', '1/9/2016 6:01', '186'],
            ['(080)40395498', '98453 94494', '1/9/2016 7:31', '1560'],
            ['97425 79921', '98453 94494', '1/9/2016 20:48', '9']
        ]

        for call in calls:
            telephones.extract_duration(call, phone_calls)

        most_time_spent = max(phone_calls, key=phone_calls.get)
        self.assertEqual('98453 94494', most_time_spent)


if __name__ == '__main__':
    unittest.main()
