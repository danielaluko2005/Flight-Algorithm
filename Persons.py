"""The Person object module"""
class Person:
    
    def __init__(self, name: str, terminal, gate, plane_used):
        """
        Args:
            name (str): The name of the passenger.
            terminal (Terminal): The Terminal object.
            gate (Gate): The Gate object.
            plane_used (Plane): The Plane object.
        """
        self.name = name
        self.terminal = terminal
        self.gate = gate
        self.plane = plane_used

    def reserve_seat(self, seat: str) -> None:
        """Function to reserve seat.
        
        Args:
            seat (str): Seat requested.
        """
        self.plane.allocate_seat(seat, self.name)

    def change_seat(self, from_seat: str, to_seat: str) -> None:
        """Relocate passenger.
        
        Args:
            from_seat (str): Initial seat.
            to_seat (str): Requested seat.
        """
        self.plane.relocate_passenger(from_seat, to_seat)
