# Build a simple command line tool that will let an admin run the following queries
# enter a unit number and return the residents who live in that unit (someone started that
# one for you but it is not returning the correct values and needs your debugging attention)

def resident_names(people_list, unit_number):
    for person in people_list:
        residents = []
        if person['unit'] == unit_number:
            resident.append(person['first_name'] + person['last_name'])
    return residents


#  enter a user's name and return back a list of all devices that user can manage
