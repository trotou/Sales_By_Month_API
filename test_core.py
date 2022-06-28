# import unittest

# class TestRomanNumeral(unittest.TestCase):
#     def test_one_to_three(self):
#         to_one = int_to_roman('1')
#         to_two = int_to_roman('2')
#         to_three = int_to_roman('3')
#         expected = ['I','II','III']
#         self.assertEqual(to_one, expected[0])
#         self.assertEqual(to_two, expected[1])
#         self.assertEqual(to_three, expected[2])


#     def test_five_to_10(self):
#         to_five = int_to_roman('5')
#         to_ten = int_to_roman('10')
#         expected = ['V','X']
#         self.assertEqual(to_five, expected[0])
#         self.assertEqual(to_ten, expected[1])


#     def test_four(self):
#         to_four = int_to_roman('4')
#         expected = 'IV'
#         self.assertEqual(to_four, expected)


#     def test_nine(self):
#         to_nine = int_to_roman('9')
#         expected = 'IX'
#         self.assertEqual(to_nine, expected)


#     def test_six_to_eight(self):
#         to_six = int_to_roman('6')
#         to_seven = int_to_roman('7')
#         to_eight = int_to_roman('8')
#         expected = ['VI', 'VII','VIII']
#         self.assertEqual(to_six, expected[0])
#         self.assertEqual(to_seven, expected[1])
#         self.assertEqual(to_eight, expected[2])


#     def test_to_fifteen(self):
#         to_fifteen = int_to_roman('50')
#         expected = 'L'
#         self.assertEqual(to_fifteen, expected)

#     def test_to_fourteen(self):
#         to_fourteen = int_to_roman('40')
#         expected = 'XL'
#         self.assertEqual(to_fourteen, expected)

#     def test_sixth_to_eight(self):
#         to_sixteen = int_to_roman('60')
#         to_seventeen = int_to_roman('70')
#         to_eighteen = int_to_roman('80')
#         expected = ['LX', 'LXX','LXXX']
#         self.assertEqual(to_sixteen, expected[0])
#         self.assertEqual(to_seventeen, expected[1])
#         self.assertEqual(to_eighteen, expected[2])

#     def test_one_hundred(self):
#         to_one_hundred = int_to_roman('100')
#         expected = 'C'
#         self.assertEqual(to_one_hundred, expected)

#     def test_to_four_hundred(self):
#         to_four_hundred = int_to_roman('400')
#         expected = 'CD'
#         self.assertEqual(to_four_hundred, expected)


#     def test_to_five_hundred(self):
#         to_five_hundred = int_to_roman('500')
#         expected = 'D'
#         self.assertEqual(to_five_hundred, expected)

#     def test_to_nine_hundred(self):
#         to_nine_hundred = int_to_roman('900')
#         expected = 'CM'
#         self.assertEqual(to_nine_hundred, expected)

#     def test_to_one_thousand(self):
#         to_one_thousand = int_to_roman('1000')
#         expected = 'M'
#         self.assertEqual(to_one_thousand, expected)

    
#     def test_to_2019(self):
#         to_2019 = int_to_roman('2019')
#         expected = 'MMXIX'
#         self.assertEqual(to_2019, expected)

