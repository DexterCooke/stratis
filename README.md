This is an example of using the the Click library to create a CLI tool. 
This tool is able to see which residents live in a specific units in an apartment building. You can move in or move out residents from apartments.

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
