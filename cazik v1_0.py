from random import randint 
from time import sleep

class coef_type:
    # тип коэффициента, например шестерка, валет, и т.п.
    
    def __init__(self, init_sign: str, init_rel_p: int, init_mult_dict):
        self.__sign = init_sign  # значек
        self.__rel_p = init_rel_p  # относительная вероятность выпадения
        self.__mult_dict = init_mult_dict  # словарь, который соединяет количество выпадений с множителем ставки
    
    def get_sign(self):
        return self.__sign
    
    def get_rel_p(self):
        return self.__rel_p
    
    def get_mult_dict(self):
        return self.__mult_dict


slots = [''] * 5  # выпавшие слоты
coefs = {  # словарь, содержащий все возможные типы коэффициентов
    '6' : coef_type('6', 100, { 2 : 0.6, 3 : 6.66 }),
    '7' : coef_type('7', 100, { 3 : 7.7 }),
    '8' : coef_type('8', 160, { 2 : 0.8, 3 : 1.1, 4 : 1.1 }),
    '9' : coef_type('9', 300, { 2 : 0.9, 3 : 1.3, 4 : 1.3, 5 : 4.5 }),
    '10' : coef_type('10', 150, { 3 : 1.5, 4 : 1.5, 5 : 5.0 }),
    'J' : coef_type('J', 100, { 2 : 1.1, 3 : 1.7, 4 : 1.7, 5 : 5.5 }),
    'Q' : coef_type('Q', 50, { 2 : 1.2, 3 : 1.9, 4 : 1.9, 5 : 6.0 }),
    'K' : coef_type('K', 25, { 2 : 1.3, 3 : 2.1, 4 : 2.1, 5 : 8.0 }),
    'A' : coef_type('A', 10, { 2 : 2.0, 3 : 8.0, 4 : 8.0, 5 : 10.0 }),
    'JP' : coef_type('jackpot', 5, { 2 : 10.0, 3 : 20.0, 4 : 50.0, 5 : 100.0 })
}


def randomize_slots(): 
    # заполняет слоты названиями типов коэффициентов в соответвии с их относительной вероятностью
    global coefs, slots 
    max_p: int = 0
    this_p: int
    
    for coef in coefs.values():
        max_p += coef.get_rel_p()
    
    for i in range(len(slots)): 
        this_p = randint(0, max_p - 1) 
        for coef_key, coef in coefs.items():
            this_p -= coef.get_rel_p()
            if (this_p < 0):
                slots[i] = coef_key
                break


def print_slots():
    # выводит на экран информацию о выпавших слотах и о джекпоте (если он выпал)
    global slots, coefs
    pace: float = 0.75  # время спина одного слота в секундах
    jackpot_counter: int = 0
    
    for coef_key in slots:
        if coef_key == 'JP':
            jackpot_counter += 1
        
        sleep(pace)
        print(coefs[coef_key].get_sign(), end=' ', flush=True)
    
    print('', end='\n')
    sleep(pace)
    
    if jackpot_counter > 1: 
        if jackpot_counter > 2: 
            print('SUPER', end=' ', flush=True) 
            sleep(pace)
        if jackpot_counter > 3: 
            print('MEGA', end=' ', flush=True) 
            sleep(pace)
        if jackpot_counter > 4: 
            print('HYPER', end=' ', flush=True) 
            sleep(pace)
        print('JACKPOT') 


def find_bet_multiplier(): 
    # возвращает множитель для ставки в зависимости от значения слотов
    mult: float = 1.0
    global slots, coefs 
    coefs_amount = { }  # словарь соединяющий ключ к типу коэффицента с количеством его выпадений
    for coef_key in coefs:
        coefs_amount[coef_key] = 0  # добавляет ключ в словарь
    
    for coef_key in slots:
        coefs_amount[coef_key] += 1
    
    no_combos: bool = True
    for coef_key, amount in coefs_amount.items(): 
        if amount > 1:
            no_combos = False
            mult_dict = coefs[coef_key].get_mult_dict()
            if amount in mult_dict:
                mult *= mult_dict[amount]
    
    if no_combos:
        mult = 0.0
    
    return mult


def new_spin(bet: int):
    # иммитирует один спин слотов, возвращает выигрыш
    randomize_slots()
    print_slots()
    profit: int = int(bet * find_bet_multiplier())
    return profit


def start_game(balance: int):
    # главная функция, запускает игру
    print('777  КАЗИК  777', end='\n\n')
    print('Ваш стартовый баланс: ', balance)
    bet: int
    profit: int
    while balance > 0:
        bet = int(input('Введите вашу ставку: '))
        if bet > balance:
            print('у вас недостаточно денег')
            continue
        
        balance -= bet
        profit = new_spin(bet)
        balance += profit
        print('Вы выиграли ', profit)
        print('Ваш баланс: ', balance)
    print('Вы проиграли все ваши деньги')


if __name__ == '__main__': 
    init_balance = 100000
    start_game(init_balance)
