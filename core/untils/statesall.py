from  aiogram.fsm.state import State, StatesGroup


class contact(StatesGroup):
    support_request = State()


class admin_message(StatesGroup):
    push = State()
    set_id = State()
    set_message = State()


# class payment(StatesGroup):
#     acc_1 = State()
#     acc_2 = State()
#     acc_3 = State()
#     acc_4 = State()
#     acc_VIP = State()
