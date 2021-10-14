import unittest
import time
from my_solution import Map
from map_gen import map_gen

LARGE_MAP = map_gen(200, 300, 3)
VERY_LARGE_MAP = map_gen(1000, 1000, 2)


class TestMap(unittest.TestCase):
    input_card = ".o..\n.o..\n....\n"
    map_1 = Map(input_card, ".ox")
    map_2 = Map(input_card, "-o,")  # non valid characters
    map_3 = Map(input_card + "..", ".ox")  # non valid lines

    def test_attributes(self):
        self.assertEqual(self.map_1.rows, 3)
        self.assertEqual(self.map_1.columns, 4)
        self.assertEqual(self.map_1.empty_char, ".")
        self.assertEqual(self.map_1.fill_char, "x")
        self.assertTrue(self.map_1.valid_characters)
        self.assertTrue(self.map_3.valid_characters)
        self.assertFalse(self.map_2.valid_characters)

    def test_valid_card(self):
        self.assertTrue(self.map_1.card_is_valid())
        self.assertEqual(self.map_1.find_largest_square(), {"side": 2, "x": 0, "y": 2})

    def test_invalid_card(self):
        self.assertFalse(self.map_2.card_is_valid())
        self.assertEqual(self.map_3.find_largest_square(), "map error\n")
        self.assertEqual(self.map_3.display_largest_square(), "map error\n")
        self.assertFalse(self.map_3.card_is_valid())
        self.assertEqual(self.map_3.find_largest_square(), "map error\n")
        self.assertEqual(self.map_3.display_largest_square(), "map error\n")


class TestMapCases(unittest.TestCase):

    def test_no_card(self):
        input_card = ""
        card = Map(input_card, ".ox")
        self.assertFalse(card.card_is_valid())
        self.assertEqual(card.display_largest_square(), "map error\n")

    def test_full_chars_only(self):
        input_card = ("x" * 20 + "\n") * 10
        card = Map(input_card, ".ox")
        self.assertTrue(card.card_is_valid())
        self.assertEqual(card.display_largest_square() + "\n", input_card)

    def test_empty_chars_only(self):
        input_card = ("." * 20 + "\n") * 20
        card = Map(input_card, ".ox")
        self.assertTrue(card.card_is_valid())
        self.assertEqual(card.display_largest_square() + "\n", input_card.replace('.', 'x'))

    def test_one_row(self):
        input_card = ".oo...."
        card = Map(input_card, ".ox")
        self.assertTrue(card.card_is_valid())
        validator = "xoo...."
        self.assertEqual(card.display_largest_square(), validator)

    def test_one_column(self):
        input_card = "o\n.\n.\n."
        card = Map(input_card, ".ox")
        self.assertTrue(card.card_is_valid())
        validator = "o\nx\n.\n."
        self.assertEqual(card.display_largest_square(), validator)

    def test_simple(self):
        input_card = ".o..\n.o..\n....\no...\n"
        card = Map(input_card, ".ox")
        self.assertTrue(card.card_is_valid())
        self.assertEqual(card.display_largest_square(), ".oxx\n.oxx\n....\no...")

    def test_exercise_example(self):
        input_card = (
            "...........................\n"
            "....o......................\n"
            "............o..............\n"
            "...........................\n"
            "....o......................\n"
            "...............o...........\n"
            "...........................\n"
            "......o..............o.....\n"
            "..o.......o................"
        )

        card = Map(input_card, ".ox")
        self.assertTrue(card.card_is_valid())
        validator = (
            ".....xxxxxxx...............\n"
            "....oxxxxxxx...............\n"
            ".....xxxxxxxo..............\n"
            ".....xxxxxxx...............\n"
            "....oxxxxxxx...............\n"
            ".....xxxxxxx...o...........\n"
            ".....xxxxxxx...............\n"
            "......o..............o.....\n"
            "..o.......o................"
        )
        self.assertEqual(
            card.display_largest_square(),
            validator
        )


class TestMapPerformance(unittest.TestCase):

    def setUp(self):
        self.start_time = time.time()

    def tearDown(self):
        t = time.time() - self.start_time
        print('%s: %.3f' % (self.id(), t))

    def test_large_map(self):
        map_ = Map(LARGE_MAP, ".ox")
        biggest_square = map_.display_largest_square()
        self.assertIsInstance(biggest_square, str)

    def test_very_large_map(self):
        map_ = Map(VERY_LARGE_MAP, ".ox")
        biggest_square = map_.display_largest_square()
        self.assertIsInstance(biggest_square, str)
