from app.constants import (REGISTER_SUCCESS_MESSAGE_TEMPLATE,
                           SCORE_MESSAGE_TEMPLATE,
                           GREETING_MESSAGE_TEMPLATE,
                           REGISTERED_MESSAGE_TEMPLATE, EXISTING_SCORE_MESSAGE)


def get_register_success_message(name, surname):
    return REGISTER_SUCCESS_MESSAGE_TEMPLATE.format(name=name, surname=surname)


def get_score_message(subject_name, score):
    return SCORE_MESSAGE_TEMPLATE.format(subject_name=subject_name, score=score)

def get_greeting_message(name, surname):
    return GREETING_MESSAGE_TEMPLATE.format(name=name, surname=surname)

def get_registered_message(user):
    return REGISTERED_MESSAGE_TEMPLATE.format(user=user)

def get_existing_score_message(subject_name, score):
    return EXISTING_SCORE_MESSAGE.format(subject_name=subject_name, score=score)