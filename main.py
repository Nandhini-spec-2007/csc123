from dataclasses import dataclass


@dataclass
class Room:
    number: int
    nightly_rate: float
    guest_name: str | None = None

    @property
    def is_available(self) -> bool:
        return self.guest_name is None


class HotelManager:
    def __init__(self, rooms: list[Room] | None = None) -> None:
        self.rooms = rooms or [
            Room(101, 85.0),
            Room(102, 85.0),
            Room(201, 120.0),
            Room(202, 120.0),
        ]

    def get_room(self, room_number: int) -> Room:
        for room in self.rooms:
            if room.number == room_number:
                return room
        raise ValueError(f"Room {room_number} does not exist.")

    def check_in(self, room_number: int, guest_name: str) -> None:
        name = guest_name.strip()
        if not name:
            raise ValueError("Guest name cannot be empty.")

        room = self.get_room(room_number)
        if not room.is_available:
            raise ValueError(f"Room {room_number} is already occupied.")
        room.guest_name = name

    def check_out(self, room_number: int) -> str:
        room = self.get_room(room_number)
        if room.is_available:
            raise ValueError(f"Room {room_number} is already vacant.")

        guest_name = room.guest_name
        room.guest_name = None
        return guest_name or ""


def show_rooms(manager: HotelManager) -> None:
    print("\nRoom  Rate/night  Status")
    print("----  ----------  ------")
    for room in manager.rooms:
        status = f"Occupied by {room.guest_name}" if not room.is_available else "Available"
        print(f"{room.number:<5} ${room.nightly_rate:<11.2f} {status}")


def run() -> None:
    manager = HotelManager()
    actions = {
        "1": "View rooms",
        "2": "Check in",
        "3": "Check out",
        "4": "Exit",
    }

    while True:
        print("\nHotel Management")
        for key, label in actions.items():
            print(f"{key}. {label}")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                show_rooms(manager)
            elif choice == "2":
                room_number = int(input("Room number: "))
                guest_name = input("Guest name: ")
                manager.check_in(room_number, guest_name)
                print(f"{guest_name.strip()} checked into room {room_number}.")
            elif choice == "3":
                room_number = int(input("Room number: "))
                guest_name = manager.check_out(room_number)
                print(f"{guest_name} checked out of room {room_number}.")
            elif choice == "4":
                print("Goodbye.")
                break
            else:
                print("Please choose an option from 1 to 4.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    run()