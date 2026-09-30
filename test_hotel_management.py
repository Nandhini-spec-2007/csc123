import unittest

from main import HotelManager, Room


class HotelManagerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manager = HotelManager([Room(1, 75.0)])

    def test_check_in_and_check_out(self) -> None:
        self.manager.check_in(1, "Avery Lee")
        self.assertFalse(self.manager.get_room(1).is_available)

        guest_name = self.manager.check_out(1)

        self.assertEqual(guest_name, "Avery Lee")
        self.assertTrue(self.manager.get_room(1).is_available)

    def test_cannot_check_in_to_occupied_room(self) -> None:
        self.manager.check_in(1, "Avery Lee")

        with self.assertRaisesRegex(ValueError, "already occupied"):
            self.manager.check_in(1, "Jordan Kim")

    def test_rejects_unknown_room_and_empty_guest(self) -> None:
        with self.assertRaisesRegex(ValueError, "does not exist"):
            self.manager.check_in(99, "Avery Lee")
        with self.assertRaisesRegex(ValueError, "cannot be empty"):
            self.manager.check_in(1, "   ")

    def test_cannot_check_out_vacant_room(self) -> None:
        with self.assertRaisesRegex(ValueError, "already vacant"):
            self.manager.check_out(1)


if __name__ == "__main__":
    unittest.main()