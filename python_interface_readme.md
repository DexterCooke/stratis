# Python command line interface

Create a python file that when run functions as a command line tool to allow a user to interact with the provided data. Complete as many of the following tasks as you can, but do not spend more than four hours total on the project. You will not be penalized for failing to finish any task.

Your tool should do the following:

* Take in the user's first and last name and only allow program access if the user is an authorized user. Assume a user is authorized if they have the property role of "Admin". Don't worry about writing additional logic to authorize the user.  **DONE**

* Allow an authorized user to input a unit number and retrieve a list of all residents of that unit. (There is an existing function named `resident_names` in stratis_interface.py that attempts to do this, but needs your debugging.) **DONE**

* Allow a user to input a first name and last name and retrieve any information we have about a resident whose name matches that first and last name. That information should include the user's unit, their role(s) on the property, and any devices that the user can control **DONE**

* Write a function that will allow the user to move in a new resident or move out an old resident. (Don't change the data in property_data.json. Instead copy the new state of the data into a file named `property_data_changes.json`.)

Try to anticipate the user's needs and create an interface that meets them.

## About the data

Sample data are in the file `property_data.json`.
The "roles" key on people objects refers to the roles a user has on that property, which impacts what devices they can control.

A person may control a device if:

* It is associated with their unit of residence.
* The device is marked as admin_accessible and the user is an admin.
  * For example, Mackenzie Carroll can control the thermostat, lights, and lock that have a unit value that matches her residence, 102. Zakiyya Shabazz can control any device that has a unit value of 201, plus any "Sunnee" light and any lock (because she is an admin and those devices all have admin_accessible marked as true.)



stratis_cli 