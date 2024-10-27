calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()
def is_contains(string, list_to_search):
    count_calls()
    # Возврящаем значение функиции
    # Проверяем вход-ть строки в список 'in', для перенебрежения регистром переводим все в  нижний регистр '.lower()'
    return string.lower() in (i.lower() for i in list_to_search)
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('UrBan', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
