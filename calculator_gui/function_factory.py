import math
import numpy as np
"""Callback will check in this file to find the function"""

def clear(event, text_history, text):
    text_history.SetValue(str(''))
    text.SetValue(str(''))

#Another Methodology which also work for callback from a different function
# def clear(event):
#     #evt_id = event.GetId()
#     evt_id = event.GetEventObject().GetParent()
#     evt_id.text_history.SetValue(str(''))
#     evt_id.text.SetValue(str(''))

def evaluate(event, text_history, text):
    """
    evaluate function finds the value of text which has been modified by different functions

    :param event: OnButtonClick section of calculator_gui\calc.fbp
    :return: evaluated **text**
    """
    try:
        text_history.SetValue(str(text.GetValue()) + str(' ='))
        text.SetValue(str(eval(text.GetValue())))
    except Exception:
        print("Error in evaluating")

def num_per(event, text):
    _value = float(text.GetValue()) / 100
    text.SetValue(str(_value))

def square_root(event, text):
    text.SetValue(str(math.sqrt(float(text.GetValue()))))

def num_power(event, text):
    text.SetValue(str(text.GetValue()) + str('**'))

def num_by_rev(self, event):
    try:
        _value = str('1') + str('/') + str(float(str(self.text.GetValue())))
        self.text.SetValue(str(eval(_value)))
    except Exception:
        print("Error in evaluating")


def multi(event, text):
    text.SetValue(str(text.GetValue()) + str('*'))


def divide(event, text):
    text.SetValue(str(float(text.GetValue())) + str('/'))


def addition(event, text):
    text.SetValue(str(text.GetValue()) + str('+'))


def substract(event, text):
    text.SetValue(str(text.GetValue()) + str('-'))


def decmal(event, text):
    text.SetValue(str(text.GetValue()) + str('.'))


def delete_char_from_right(event,text):
    current_string = str(text.GetValue())
    text.SetValue(current_string[:len(current_string) - 1])


def num_factorial(event, text_history, text):
    try:
        _value = math.gamma(float(text.GetValue()))
        text_history.SetValue(str(text.GetValue()) + str('!'))
        text.SetValue(str(_value))
    except OverflowError as e:
        print(e)

# number input from 0-9
def number_input_zero(event, text):
    if not text.GetValue():
        text.SetValue(str(0))
    else:
        text.SetValue(str(text.GetValue()) + str(0))


def number_input_one(event, text):
    if not text.GetValue():
        text.SetValue(str(1))
    else:
        text.SetValue(str(text.GetValue()) + str(1))


def number_input_two(event, text):
    if not text.GetValue():
        text.SetValue(str(2))
    else:
        text.SetValue(str(text.GetValue()) + str(2))


def number_input_three(event, text):
    if not text.GetValue():
        text.SetValue(str(3))
    else:
        text.SetValue(str(text.GetValue()) + str(3))


def number_input_four(event, text):
    if not text.GetValue():
        text.SetValue(str(4))
    else:
        text.SetValue(str(text.GetValue()) + str(4))


def number_input_five(event, text):
    if not text.GetValue():
        text.SetValue(str(5))
    else:
        text.SetValue(str(text.GetValue()) + str(5))


def number_input_six(event, text):
    if not text.GetValue():
        text.SetValue(str(6))
    else:
        text.SetValue(str(text.GetValue()) + str(6))


def number_input_seven(event, text):
    if not text.GetValue():
        text.SetValue(str(7))
    else:
        text.SetValue(str(text.GetValue()) + str(7))


def number_input_eight(event, text):
    if not text.GetValue():
        text.SetValue(str(8))
    else:
        text.SetValue(str(text.GetValue()) + str(8))


def number_input_nine(event, text):
    if not text.GetValue():
        text.SetValue(str(9))
    else:
        text.SetValue(str(text.GetValue()) + str(9))