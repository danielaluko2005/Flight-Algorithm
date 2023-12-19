class Airport:
    """Airport Class."""
    def __init__(self, name) -> None:
        """
        Args:
            name (str): Airport name
        """
        self.name = name
        self.list_of_terminals = []

    def num_of_terminals(self, num):
        """
        Args:
            num (int): Number of terminals
        Returns:
            int: Number of Terminals.
        """
        self.list_of_terminals = [Terminal(input(f"Enter Name of Terminal {i + 1}:- ")) for i in range(num)]
        return num

class Terminal:
    def __init__(self, terminal_name):
        """
        Args:
            terminal_name (str): Name of the airport.
        """
        self.terminal_name = terminal_name
        self.gates_overview = {}
        self.gates = {}

    def terminal_gates(self):
        """To set the Terminals and Gates in the airport
        Returns:
            dict: 
        """
        number_of_letters = int(input(f"How many letters do you want for {self.terminal_name}:- "))
        for int_letter in range(65, 65 + number_of_letters):
            letter = chr(int_letter)
            num_gates_per_letter = int(input(f"How many Gates do you want in '{letter}' in {self.terminal_name}:- "))
            self.gates_overview[letter] = num_gates_per_letter

        self.gates = {f"{gate}{index + 1}": None for gate, num_gates in self.gates_overview.items() for index in range(num_gates)}

        return self.gates
    
    def print_terminals_gates(self):
        print(f"The gates available in {self.terminal_name}: ")
        for gate in self.gates:
            print(gate)

class Gate:
    """Each Gate in the terminal."""
    def __init__(self, gate_name, terminal):
        """
        Args:
            gate_name (str): The name of the gate. i.e(A1...)
            terminal (Terminal): An instance of the terminal it is at.
        Raises:
            ValueError: if the Gate name isn't in the Terminal
        """
        if gate_name not in terminal.gates:
            raise ValueError(f"The gate '{gate_name}' doesn't exist in this Terminal.")
        
        self.gate_name = gate_name
        self.terminal = terminal

    def allocate_gate(self, flight_number):
        """Allocate the gate with a flight number.
        Args:
            flight_number (str): Flight number.
        """
        if self.terminal.gates[self.gate_name] is None:
            self.terminal.gates[self.gate_name] = flight_number
            print("Flight Allocated...")
        else:
            raise ValueError("Gate not available.")
            
    def get_allocated_gate_for_flight(self):
        """Returns flight number"""
        return self.terminal.gates[self.gate_name]
