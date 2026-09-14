

airport_info = ("OUL", 1, "14-09-2026")

allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}

restricted_destinations = {"Moscow", "Pyongyang"}

flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": ["Alice Wong", "David Kim", "Fatima Ali"]
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": ["Chen Wei", "George Smith"]
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": ["Hana Lee", "Maria Garcia", "Noah Wilson"]
    }
}


def find_flight(flights, flight_number):
    if type(flight_number) != str:
        return None
    target = flight_number.strip().upper()
    for key in flights:
        if key.upper() == target:
            return key
    return None


def passenger_exists(passengers, passenger_name):
    if type(passenger_name) != str:
        return False
    target = passenger_name.strip().lower()
    for name in passengers:
        if name.lower() == target:
            return True
    return False


def check_in_passenger(flights, flight_number, passenger_name, restricted_destinations):
    key = find_flight(flights, flight_number)
    if key == None:
        return "FLIGHT_NOT_FOUND"

    if type(passenger_name) != str or passenger_name.strip() == "":
        return "EMPTY_NAME"

    name = passenger_name.strip().title()
    flight = flights[key]

    if flight["destination"] in restricted_destinations:
        return "RESTRICTED"

    if passenger_exists(flight["passengers"], name):
        return "DUPLICATE"

    if len(flight["passengers"]) >= flight["capacity"]:
        return "FULL"

    flight["passengers"].append(name)
    return "OK"


def remove_passenger(flights, flight_number, passenger_name):
    key = find_flight(flights, flight_number)
    if key == None:
        return "FLIGHT_NOT_FOUND"

    if type(passenger_name) != str:
        return "PASSENGER_NOT_FOUND"

    target = passenger_name.strip().lower()
    names = flights[key]["passengers"]

    for i in range(len(names)):
        if names[i].lower() == target:
            names.pop(i)
            return "OK"

    return "PASSENGER_NOT_FOUND"


def change_gate(flights, flight_number, new_gate, allowed_gates):
    key = find_flight(flights, flight_number)
    if key == None:
        return "FLIGHT_NOT_FOUND"

    if type(new_gate) != str:
        return "INVALID_GATE"

    gate = new_gate.strip().upper()

    ok = False
    for g in allowed_gates:
        if g.upper() == gate:
            ok = True

    if not ok:
        return "INVALID_GATE"

    flights[key]["gate"] = gate
    return "OK"


def flight_status(flight):
    cap = flight["capacity"]
    num = len(flight["passengers"])

    if cap == 0:
        return "FULL"

    pct = num / cap * 100

    if pct >= 100:
        return "FULL"
    elif pct >= 75:
        return "ALMOST FULL"
    else:
        return "AVAILABLE"


def sorted_manifest(flights, flight_number):
    key = find_flight(flights, flight_number)
    if key == None:
        return None
    return sorted(flights[key]["passengers"])


def total_passengers(flights):
    total = 0
    for f in flights.values():
        total = total + len(f["passengers"])
    return total


def any_full_flight(flights):
    for f in flights.values():
        if len(f["passengers"]) >= f["capacity"]:
            return True
    return False


def all_flights_have_passengers(flights):
    for f in flights.values():
        if len(f["passengers"]) == 0:
            return False
    return True