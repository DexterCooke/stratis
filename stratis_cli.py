from collections import defaultdict
from os import path
import json
import click

class Stratis:

    def __init__(self, first_name, last_name):
        self.data = self._read_file('property_data.json')
        self.first_name = first_name
        self.last_name = last_name

        #Automatically create and fill property_data_changes.json with current residents
        if not path.exists('property_data_changes.json'):
            people_list = self._get_people()
            self._write_file(people_list, 'property_data_changes.json')

        self.valid_residents = self._read_file('property_data_changes.json')


    def is_resident_valid(self, first_name, last_name):
        """Determines if resident lives in the building"""
        for idx, val in enumerate(self.valid_residents):
            if first_name == str(self.valid_residents[idx]['first_name']) and last_name == str(self.valid_residents[idx]['last_name']):
                return True
        return False
            
 
    def _read_file(self, file):
        """Read json file"""
        with open(file) as f:
            data = json.load(f)
        return data

    def _write_file(self, data, file):
        """Write json file"""
        with open(file, 'w') as f:
            json.dump(data, f)
            # f.write("\n")


    def _is_user_admin(self):
        """
        Checks if user has admin rights
        Returns: bool
        """
        people_list = self._get_people()

        for idx, val in enumerate(people_list):
            if self.first_name == people_list[idx]['first_name'] and self.last_name == people_list[idx]['last_name']:
                if 'Admin' in people_list[idx]['roles']:
                    return True
        print('No administrator privilages')
        return False

    def resident_names(self, unit_number):
        """
        Returns a list of all residents in unit
        Returns: json
        """
        if self._is_user_admin():
            residents = []
            people_list = self._get_people()
            for idx, val in enumerate(people_list):
                if str(unit_number) == people_list[idx]['unit']:
                    residents.append((people_list[idx]['first_name'], people_list[idx]['last_name']))
            
            #if resident not in property_data.json then check property_data_changes.json
            if not residents:
                for idx, val in enumerate(self.valid_residents):
                    if str(unit_number) == self.valid_residents[idx]['unit']:
                        residents.append((self.valid_residents[idx]['first_name'], self.valid_residents[idx]['last_name']))
            if residents:
                print(json.dumps(residents))
            else:
                print("Unit is empty")
                    

    def resident_info(self, res_first_name, res_last_name):
        """
        Returns a json list of devices and roles of resident
        Returns: json
        """
        if not self.is_resident_valid(res_first_name, res_last_name):
            print("Resident doesn't live in building")
            return 

        if self._is_user_admin():
            is_resident_admin = False
            people_list = self._get_people()
            for idx, val in enumerate(people_list):
                if res_first_name == people_list[idx]['first_name'] and res_last_name == people_list[idx]['last_name']:
                    if 'Admin' in people_list[idx]['roles']:
                        is_resident_admin = True
                    print(self._get_devices_for_resident(people_list[idx]['unit'], is_resident_admin))
                    return 

            
            for idx, val in enumerate(self.valid_residents):
                if res_first_name == self.valid_residents[idx]['first_name'] and res_last_name == self.valid_residents[idx]['last_name']:
                    #dummy data for resident in property_data_changes.json
                    data = {
                        "locks" : ['LockNess'],
                        "lights": ['Sunnee'],
                        "roles" : ['Resident'],
                        "unit"  : self.valid_residents[idx]['unit'],
                        "thermostat" : ['Warm-Me']
                    }
                    print(json.dumps(data))

    def _get_devices_for_resident(self, unit_number, is_resident_admin):
        """ 
        Helper function that iterates through the self.data attribute to return the devices associated
        with resident
        """
        resident_data = {}
        thermostats = self.data['devices']['thermostats']
        lights = self.data['devices']['lights']
        locks = self.data['devices']['locks']
        people_list = self._get_people()
        resident_data['unit'] = int(unit_number)

        #Create dictionaries with resident controlled devices
        resident_thermostats = self._get_resident_controlled_device(thermostats, is_resident_admin, unit_number, 'thermostat')
        resident_lights = self._get_resident_controlled_device(lights, is_resident_admin, unit_number, 'lights')
        resident_locks = self._get_resident_controlled_device(locks, is_resident_admin, unit_number, 'locks')

        #Create dictionary with resident roles
        for idx, val in enumerate(people_list):
            if unit_number == people_list[idx]['unit']:
                resident_data['roles'] = people_list[idx]['roles']

        #Merge dictionaries 
        resident_data.update(resident_thermostats)
        resident_data.update(resident_lights)
        resident_data.update(resident_locks)

        return json.dumps(resident_data)

    def _get_resident_controlled_device(self, device, is_resident_admin, unit_number, device_name):
        """Return dict of device controlled by resident"""
        resident_data = defaultdict(list)
        for idx, val in enumerate(device):
            if int(unit_number) == device[idx]['unit'] \
            or is_resident_admin and device[idx]['admin_accessible'] == 'true':
                if device[idx]['model'] not in resident_data[device_name]:
                    resident_data[device_name].append(device[idx]['model'])
        return resident_data


    def _get_people(self):
        """ Returns list list of people from data attribute """
        return self.data['people']

    def move_resident(self, is_moved_in, res_first_name, res_last_name, unit_number):
        """Move resident in or out of unit and update property_data_changes.json"""
        if str(is_moved_in) == 'true':
            data = {
                'first_name': res_first_name,
                'last_name' : res_last_name,
                'roles'     : ['Resident'],
                'unit'      : unit_number
            }
            if data not in self.valid_residents:
                self.valid_residents.append(data)
                self._write_file(self.valid_residents, 'property_data_changes.json')

        if str(is_moved_in) == 'false':
            for idx, val in enumerate(self.valid_residents):
                if res_first_name == self.valid_residents[idx]['first_name'] and res_last_name == self.valid_residents[idx]['last_name']:
                    del(self.valid_residents[idx])
                    self._write_file(self.valid_residents, 'property_data_changes.json')
            


pass_stratis = click.make_pass_decorator(Stratis)

@click.group()
@click.argument('user_first_name', metavar='<user_first_name>')
@click.argument('user_last_name', metavar='<last_first_name>')
@click.pass_context
def cli(ctx, user_first_name, user_last_name):
    """Admin users are able to get data on residents"""
    ctx.obj = Stratis(user_first_name, user_last_name)


@cli.command()
@click.argument('res_first_name', metavar='<res_first_name>')
@click.argument('res_last_name', metavar='<res_last_name>')
@pass_stratis
def resident_info(stratis, res_first_name, res_last_name):
    """Get resident's unit number, devices they control, and role """
    stratis.resident_info(res_first_name, res_last_name)


@cli.command()
@click.argument('unit_number')
@pass_stratis
def resident_names(stratis, unit_number):
    """Get names of resident(s) in unit """
    stratis.resident_names(unit_number)

@cli.command()
@click.argument('is_moved_in', metavar='true')
@click.argument('res_first_name', metavar='<res_first_name>')
@click.argument('res_last_name', metavar='<res_last_name>')
@click.argument('unit_number')
@pass_stratis
def move_in(stratis, is_moved_in, res_first_name, res_last_name, unit_number):
    """Move in true, move out false """
    stratis.move_resident(is_moved_in, res_first_name, res_last_name, unit_number) 

if __name__ == '__main__':
    cli()