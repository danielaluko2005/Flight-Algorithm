import airtravel
from Terminal_and_gates import  Gate,Airport
from Persons import Person
def main():
    """Creates flights objects
    
        main driver
    """

    """Creates a Terminal1 object"""
    SLC_airport=Airport("SLC airport")
    SLC_airport.num_of_terminals(2)
    SLC_airport.list_of_terminals[0].terminal_gates()
    SLC_airport.list_of_terminals[1].terminal_gates()

    """Create a GateA1 object and allocate the Gate to a Flight. Pass the instance of the Terminal1 created previously as an argument"""
    GateA1=Gate("A1",SLC_airport.list_of_terminals[0])
    GateA1.allocate_gate("BA758")

    """Create a plane object"""
    first_plane=airtravel.Flight(GateA1.get_allocated_gate_for_flight(),airtravel.AirbusA319("G-EUPT"))

    """Create a person object"""
    person1=Person("Daniel",SLC_airport.list_of_terminals[0],GateA1,first_plane)
    person1.reserve_seat("12A")

    """Create another person object with the same Terminal object as the previous one but different Gates."""
    GateA2=Gate("A2",SLC_airport.list_of_terminals[0])
    GateA2.allocate_gate("EH247")
    second_plane=airtravel.Flight(GateA2.get_allocated_gate_for_flight(),airtravel.AirbusA319("H-GPTA"))
    person2=Person("Nifemi",SLC_airport.list_of_terminals[0],GateA2,second_plane)
    person2.reserve_seat("12A")

    """Create another person object with different Terminal object."""
    GateB1=Gate("B1",SLC_airport.list_of_terminals[1])
    GateB1.allocate_gate("TH312")
    third_plane=airtravel.Flight(GateB1.get_allocated_gate_for_flight(),airtravel.Boeing777("G-IPRA"))
    person3=Person("Marley",SLC_airport.list_of_terminals[1],GateB1,third_plane)
    person3.reserve_seat("13A")
    

if __name__=="__main__":
    main()