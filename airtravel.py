"""Model For Aircraft Flights"""

class Flight:
    """A Flight with a particular passenger aircraft"""

    def __init__(self,number,aircraft):
        """Validate the fight number and initialize the parameters of this method,

            Args:
                number(str): the flight number.
                aircrat(str):The aircraft used for this flight.

            Raise:
                ValueError: The first two Letters isn't an ALPHABET.
                ValueError: The first two characters isn't capitalized.
                ValueError: If greater 9999 and if the second character to the last isn't numeric.

        """

        if not number[:2].isalpha():
            raise ValueError(f"No airline code '{number}'.")
        
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")
        
        if not (number[2:].isdigit() and int(number[2:])<=9999):
            raise ValueError(f"Invalid route number '{number}'")
        
        self._number=number
        self._aircraft=aircraft

        rows,seats=self._aircraft.seating_plan()
        self._seating=[None]+ [{letter:None for letter in seats} for _ in rows]

    def number(self):
        """Get the flight number of the flight object.
        Returns:
            (str):flight number.
        """
        return self._number
    
    def airline(self):
        """Get the airline code of the Flight object
        Returns:
            (str): two-letter airline code.
        """
        return self._number[:2]
    
    def aircraft_model(self):
        """Get Model of the aircraft used for the flight
        Returns:
            (str): the model of the aircraft used for the flight.
        """
        return self._aircraft.model()
    
    def _parse_seat(self,seat):
        """Determine the row and seat letter.
        Args:
            (str):seat
        raise:
            ValueError:Invalid seat letter.
            ValueError:Invalid seat row.
            ValueError: Invalid row number.
        Returns:
            type(tuple):row number and seat letter.
        """
        row_numbers,seat_letters=self._aircraft.seating_plan()

        letter=seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter '{letter}'")
        
        row_text=seat[:-1]
        try:
            row=int(row_text)
        except ValueError:
            raise ValueError(f"Invalid sit row '{row_text}'")
        
        if row not in row_numbers:
            raise ValueError(f"Invalid row number `{row}`")
        
        return row,letter
    
    def allocate_seat(self,seat,passenger):
        """Assign seat to passenger
        Args:
            seat(str): seat
            passenger: passenger
        Raise:
            ValueError: seat is occupied or invalid letter input for the flight object.
        """
        row,letter=self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat '{seat}' is already occupied")
        
        self._seating[row][letter]=passenger
        print("Seat assigned Succesfully.")

    def relocate_passenger(self,from_seat,to_seat):
        """Relocate passenger
        Args:
            from_seat(str):initial seat
            to_seat(str): Requested seat
        Raises:
            ValueError:  if the initial_seat isn't valid for the aircraft object or is empty.
            ValueError:  if the requested seat is occupied.
        """
        from_row,from_letter=self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat.")
        
        to_row,to_letter=self._parse_seat(to_seat)
        
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat '{to_seat}' is occupied.")
        
        self._seating[to_row][to_letter]=self._seating[from_row][from_letter]
        self._seating[from_row][from_letter]=None
        print("Seat Changed succesfully.")

    def num_available_seats(self):
        """Get number of available sits in flight"""
        return sum(sum(1 for s in row.values() if s is None) for row in self._seating if row is not None)
    
    def num_passengers(self):
        """
        Get number of available seats on the Flight object
        Return:
            (int): number of seats on the flight
        """
        return sum(sum(1 for s in row.values() if s is not None) for row in self._seating if row is not None)

    
    def make_boarding_pass(self,card_printer):
        """Print the Flight ticket
        Arg:
            card_printer(function): The card Printer function.
        """

        for passenger,seat in sorted(self._passenger_seats()):
            card_printer(passenger,seat,self.number(),self.aircraft_model())

    def _passenger_seats(self):
        """Obtains each occupied seat alongside the passenger
        """

        row_numbers,seat_letters= self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger=self._seating[row][letter]
                if passenger is not None:
                    yield (passenger,f'{row}{letter}')



class Aircraft:
    """Aircraft

    Args:
        Aircraft(class): The aircraft class.
    """

    def __init__(self,registration):
        """Initializes the aircraft class
        
            Args:
                registration(str): Registration number of the flight.
        """

        self.registration=registration
        
    def registration(self):
        """
        returns:
            str(): Registration Number.
        """
        return self.registration
    
    def num_seats(self):
        """
        returns:
            (int): total number of seats on the flight.
        """
        rows,row_seats=self.seating_plan()
        return len(rows)*len(row_seats)
    
    def terminal(self):
        """To set what terminal the plane is.
        
        Returns:
            str():Tells the terminal
        """
        set_terminal=input("Enter Terminal:- ")
        return set_terminal
    
    def gate(self):
        """What Gate the plane is in.
        Returns:
            str(): Tells what gate the aircraft shoukd be.
        """
        set_gate=input("What Gate should it be:- ")

class AirbusA319(Aircraft):
    """Aircraft Airbus A319
    ARGS:
        Aircraft(class): The Aircraft class.
    """

    def model(self):
        """returns
            (str): model of the Aircraft.
        """
        return "AirbusA319"
    
    def seating_plan(self):
        """
        returns:
            (str): rows of the aircraft and seat letters
        """
        return range(1,23),"ABCDEF"
    

class Boeing777(Aircraft):
    """Aircraft Boeing777
    ARGS:
        Aircraft(class): The Aircraft class.
    """

    def model(self):
        """returns
            (str): model of the Aircraft.
        """
        return "Boeing777"
    
    def seating_plan(self):
        """
        returns:
            (str): rows of the aircraft and seat letters
        """
        return range(1,56),"ABCDEFGHJK"
    

    

def make_flight():
    """Create flight object
    returns:
        (tuple): 2 Flight object.
    """

    f=Flight("BA758",AirbusA319("G-EUPT"))
    f.allocate_seat("3A","Thompson Larry")
    f.allocate_seat("7A","Klay Ramsey")
    f.allocate_seat("4B","Ramsey Ozil")
    f.allocate_seat("2B","Nico Omilana")
    f.allocate_seat("7D","Robin Mclery")

    b=Flight("AF72",Boeing777("F-GSPS"))
    b.allocate_seat("4A","Romy Jesse")
    b.allocate_seat("4D","Lazarus Dave")
    b.allocate_seat("7A","Santan Dave")
    b.allocate_seat("2C","Digne Luca")

    return f,b

def console_card_printer(passenger,seat,flight_number,aircraft):
    """Print boarding pass for passengers
    
    Args:
        passenger(str): name of the passengers
        seat(str): seat number
        flight_number: flight number
        aircraft(str): aircaft model
    """

    output="| Name: {0}"  \
            " |Flight: {1}" \
            " Seat: {2}" \
            " Aircraft:{3}" \
            " |".format(passenger,flight_number,seat,aircraft)
    banner="+"+"-"*(len(output)-2)+"+"
    border="|"+" "*(len(output)-2)+"|"
    lines=[banner,border,output,border,banner]
    card='\n'.join(lines)
    print(card)
    print()


