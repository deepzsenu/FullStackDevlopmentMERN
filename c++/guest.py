def combine_guests(guests1, guests2):
    combined_guests = guests2.copy()
    combined_guests.update(guests1)
    return combined_guests

Ricks_guests = {"Adam": 2, "Camila": 3, "David": 1, "3amal": 3, "Charley": 2, "Titus": 1, "Raj": 4}
Tessas_guests = {"David": 4, "Noemi": 1, "Raj": 2, "Adam": 1, "Sakira": 3, "Chidi": 5}

print(combine_guests(Ricks_guests, Tessas_guests))
