import requests
import json
from sys import argv, exit

DOMAIN = 'http://localhost:8000'

def get_persons():
    r = requests.get(DOMAIN + '/api/list_persons')
    with open('persons.json', 'w') as f:
        f.write(r.text)
    ## why??
    persons_json = json.loads(r.text) ## make it json
    persons_dict = json.loads(persons_json) ## make it dict.. .
    print(persons_dict[1])
    num_persons = len(persons_dict)
    print('succesfully wrote %s persons to file persons.json' %  num_persons)

def add_person(name, full_name, email): # is it ok to use same names in 
                                        # functions call and def?
    new_person_data = {
        'name': name,
        'full_name': full_name,
        'email': email,
    }
    print('Adding person...')
    r = requests.post(DOMAIN + '/api/add_person', data = new_person_data)
    with open('log.html', 'w') as f:
        f.write(r.text)

def delete_person(short_name_substing):
    payload = {'substr': short_name_substing}
    r = requests.delete(DOMAIN + '/api/delete_persons/' + short_name_substing)
    print('Deleting person...')
    with open('log.html', 'w') as f:
        f.write(r.text)



def check_parameters(argv):
    if len(argv) < 2:
        print ('You should enter at least 1 parameter')
        exit(1)
    elif len(argv) == 2 and argv[1] == 'list':
        return get_persons()
    elif len(argv) == 3 and argv[1] == 'del':
        return delete_person(argv[2])
    elif len(argv) == 5 and argv[1] == 'add':
        name = argv[2]
        full_name = argv[3]
        email = argv[4]
        add_person(name, full_name, email)

check_parameters(argv)

