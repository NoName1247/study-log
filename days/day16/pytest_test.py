from jsonlesson import *

def setup_function():
    spisok.clear()

def add_test():
    result = add('test', 'test_test_test_test')
    assert len(spisok) ==1
    assert result['title'] == 'test'
    assert result['body'] == 'test_test_test_test'
    assert result['status'] == False

def test_done():
    result = add('test', 'test_test_test_test')
    id = result['id']
    assert done(id) == f'element {id} is Done'

def test_done_not_found ():
    assert done('123123123') == 'Not found'


def test_delete_task_success():
    result = add("Тест", "Описание")
    task_id = result['id']

    # Удаляем задачу
    response = dell(task_id)

    assert response == 'sucsses'
    assert len(spisok) == 0  # Словарь должен стать пустым
    assert task_id not in spisok


# Тест 5: Проверяем вывод пустого списка
def test_list_empty():
    response = lis()
    assert response == 'list is empty'