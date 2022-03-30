from random import randint
slots_repr: list[int] = [0] * 5
coef_size: int = 11
coefs: list[int] = [0] * coef_size


def seed_slots( cap: int = 10 ) -> None:
    # заполняет слоты случайными числами
    # cap - размер интервала на один тап коефицента
    global coef_size, slots_repr
    cap *= coef_size
    for i in range(len(slots_repr)):
        slots_repr[i] = randint(0, cap)


def set_coefs() -> None:
    # устанавливает коефиценты в соответсви со слотами
    global coef_size, slots_repr, coefs
    for i in range(len(slots_repr)):
        coefs[slots_repr[i] // coef_size] += 1


def clear_coefs() -> None:
    global coefs
    for i in range(len(coefs)):
        coefs[i] = 0

