from random​import​randint 


class coef_type:
    # тип коэффициента, например шестерка, валет, и т.п.
    
    def __init__(self, init_sign: str, init_rel_p: int, init_coef_dict):
        self.__sign = init_sign  # значек
        self.__rel_p = init_rel_p  # относительная вероятность выпадения
        self.__coef_dict = init_coef_dict  # словарь, который соединяет количество выпадений с множителем ставки
    
    def get_sign(self):
        return self.__sign
    
    def get_rel_p(self):
        return self.__rel_p
    
    def get_coef_dict(self):
        return self.__coef_dict
    


slots = [''] * 5  # выпавшие слоты
coefs = {  # словарь, содержащий все возможные типы коэффициентов
    '6' : coef_type('6', 15, { 2 : 0.6, 3 : 6.66 }),
    '7' : coef_type('7', 13, { 3 : 7.7 }),
    '8' : coef_type('8', 11, { 2 : 0.8, 3 : 1.1, 4 : 1.1 }),
    '9' : coef_type('9', 9, { 2 : 0.9, 3 : 1.3, 4 : 1.3, 5 : 4.5 }),
    '10' : coef_type('10', 7, { 3 : 1.5, 4 : 1.5, 5 : 5.0 }),
    'J' : coef_type('J', 5, { 2 : 1.1, 3 : 1.7, 4 : 1.7, 5 : 5.5 }),
    'Q' : coef_type('Q', 4, { 2 : 1.2, 3 : 1.9, 4 : 1.9, 5 : 6.0 }),
    'K' : coef_type('K', 3, { 2 : 1.3, 3 : 2.1, 4 : 2.1, 5 : 8.0 }),
    'A' : coef_type('A', 2, { 2 : 2.0, 3 : 8.0, 4 : 8.0, 5 : 10.0 }),
    'JP' : coef_type('jackpot', 1, { 2 : 10.0, 3 : 20.0, 4 : 50.0, 5 : 100.0 })
}


def seed_slots(): 
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
    global slots, coefs
    jackpot_counter: int = 0
    
    for coef_key in slots:
        if coef_key == 'JP':
            jackpot_counter += 1
        
        print(coefs[coef_key].get_sign(), end=' ')
    
    print('', end='\n')
    
    if jackpot_counter >= 2: 
        if jackpot_counter >= 3: 
            print( 'SUPER', end=' ') 
        if jackpot_counter >= 4: 
            print( 'MEGA', end=' ' ) 
        if jackpot_counter >= 5: 
            print( 'HYPER', end=' ' )
        print( 'JACKPOT' ) 


def find_bet_multiplier(): 
    # возвращает множитель для ставки в зависимости от значения слотов
    mult: float = 1.0
    global slots, coefs 
    coefs_amount = { }
    
    for coef_key in coefs:
        coefs_amount[coef_key] = 0
    
    for coef_key in slots:
        coefs_amount[coef_key] += 1
    
    no_combos: bool = True
    for coef_key, amount in coefs_amount.items(): 
        if amount > 1:
            no_combos = False
            mult_dict = coefs[coef_key].get_coef_dict()
            if amount in mult_dict:
                mult *= mult_dict[amount]
    
    if no_combos:
        mult = 0.0
    
    return mult


def new_roll():
    bet = int(input('Введите вашу ставку: '))
    seed_slots()
    print_slots()
    print('Вы выиграли ', bet * find_bet_multiplier())

if __name__ == '__main__':
    while True:
        new_roll()
