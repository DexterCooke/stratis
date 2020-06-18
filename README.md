How to run:
1. create a virtual environment: >virtualenv virtualenv
2. > source venv/bin/activate
3. > python -m pip install --editable .
4. typing 'stratis' should reveal a help menu


Only authorized residents can see this out of any the commands. 

For example, to get Zakiyya Shabazz's info type:
    > stratis Ty Adams resident-info Zakiyya Shabazz
output:
    > {"locks": ["SkeletonKey", "LockNess"], "lights": ["Bright Ideas", "Sunnee"], "roles": ["Admin", "Resident"], "unit": 201, "thermostats": ["Warm-Me"]}


To get residents in unit 301 type:
    > stratis Ty Adams resident-names 301
output: 
    > ["Dorothea Brooke", "Jian Ma"]


To move in resident type:
    > stratis Ty Adams move-in true Dexter Cooke 999
output:
    > Resident moved in

To move out resident type:
    > stratis Ty Adams move-in false Dexter Cooke 999
output:
    > Resident moved out


NOTES:
    1. For resident Duane Valasquez I changed the 'a' to a regular 'a' because I didn't know how to handle that character
    2. I noticed Mackenzie Carroll, unit 102 doesnt' have thermostat and unit 101 has two thermostats, I didnt' change the json
       file but wasn't sure if thats typo.






