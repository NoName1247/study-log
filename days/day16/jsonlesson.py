from random import randint
import json
import sys


def save_tasks(tasks_dict):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks_dict, file, ensure_ascii=False, indent=4)

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


spisok = load_tasks()


def add ( title:str,body:str):
    newid = str(randint(100000, 999999))
    while newid in spisok:
        newid = str(randint(100000, 999999))

    spisok[newid]={
        'title': title,
        'body': body,
        'status':False
    }
    return {
        "id": newid,
        'title': title,
        'body': body,
        'status': False,
        'message': 'sucssesful'
            }

def dell (id:str):
    if id in spisok:
        del spisok[id]
        return 'sucsses'
    else:
        return 'Not Found'


def lis ():
    if len(spisok) ==0:
        return 'list is empty'
    for i in spisok:
        print(i, spisok[i]['title'],spisok[i]['body'],f"task is done:{spisok[i]['status']}")


def done (id:str):
    if id in spisok:
        spisok[id]['status']=True
        return f'element {id} is Done'
    return 'Not found'




if __name__ == '__main__':
    if len(sys.argv) <2:
        print('вы чет не указали')
        sys.exit(400)

    comand = sys.argv[1]

    if comand =='add':
        if len(sys.argv) != 4:
            print('wordssss')
            sys.exit(1)
        else:
            title = sys.argv[2]
            body = sys.argv[3]
            add(title,body)
            save_tasks(spisok)
    elif comand == 'lis':
        lis()
        save_tasks(spisok)
    elif comand =='del':
        id = sys.argv[2]
        dell(id)
        save_tasks(spisok)

    elif comand=='done':
        id = sys.argv[2]
        done(id)
        save_tasks(spisok)

