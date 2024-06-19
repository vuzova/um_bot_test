ACTION_LOGIN = 'Войти'
ACTION_REGISTER = 'Зарегистрироваться'

ACTION_ENTER_SCORES = 'Внести баллы'
ACTION_SHOW_SCORES = 'Посмотреть свои баллы'

START_MESSAGE = 'Привет, дорогой ученик! Это бот для сбора баллов.'
SCORE_SAVED_MESSAGE = 'Баллы успешно сохранены!'
SCORE_UPDATE_MESSAGE = 'Баллы обновлены!'

REGISTER_NAME_PROMPT = 'Введите ваше имя'
REGISTER_SURNAME_PROMPT = 'Теперь введите вашу фамилию'
SELECT_SUBJECT_PROMPT = 'Выберите предмет'
ENTER_SCORE_PROMPT = 'Введите количество баллов'
SELECT_ACTION_PROMPT = 'Выберите действие'

INVALID_SCORE_MESSAGE = 'Пожалуйста, введите число.'
INVALID_SCORE_RANGE_MESSAGE = 'Количество баллов не может быть меньше 0 или больше 100.'
INVALID_USER_MESSAGE = 'Вы не зарегистрированы. Пожалуйста, зарегистрируйтесь или авторизуйтесь.'


REGISTER_SUCCESS_MESSAGE_TEMPLATE = 'Регистрация завершена!\n' \
                                     'Ваше имя: {name}\n' \
                                     'Ваша фамилия: {surname}'

SCORE_MESSAGE_TEMPLATE = '{subject_name}: {score}'
GREETING_MESSAGE_TEMPLATE = 'Привет, {name} {surname}!'
REGISTERED_MESSAGE_TEMPLATE = "Вы уже зарегистрированы как {user.name} {user.surname}."
EXISTING_SCORE_MESSAGE = "У вас уже есть балл {score} по предмету {subject_name}."
