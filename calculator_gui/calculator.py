"""
The Project is to create a Gui for Calculator. Python code for GUI is generated with `WxFormBuilder <http://www.wxformbuilder.org>`_.
One need to open .fbp (e.g.calc.fsb for our code) and modify the GUI. Then click generate, to generate corresponding python code (gui.py)
Different functions used in put OnButtonClick for GUI is defined here.

    >>> # importing wx files
    >>> # import the newly created GUI file
    >>> # importing * : to enable writing sin(13) instead of math.sin(13)
    >>> # inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
"""

import wx
import gui
import math

class CalcCall(gui.MyFrame):
    """This object is called for the CalC GUI"""
    def __init__(self):
        # initialize parent class
        gui.MyFrame.__init__(self, parent=None)
        # Connect Events
        self.num_perc.Bind(wx.EVT_BUTTON, self.num_per)
        self.sqrt.Bind(wx.EVT_BUTTON, self.square_root)
        self.x_power.Bind(wx.EVT_BUTTON, self.num_power)
        self.num_rev.Bind(wx.EVT_BUTTON, self.num_by_rev)
        self.Clear_Entry.Bind(wx.EVT_BUTTON, self.num_factorial)
        self.clean.Bind(wx.EVT_BUTTON, self.clear)
        self.m_button12.Bind(wx.EVT_BUTTON, self.delete_char_from_right)
        self.m_button13.Bind(wx.EVT_BUTTON, self.divide)
        self.seven.Bind(wx.EVT_BUTTON, self.number_input_seven)
        self.eigth.Bind(wx.EVT_BUTTON, self.number_input_eight)
        self.nine.Bind(wx.EVT_BUTTON, self.number_input_nine)
        self.multiply.Bind(wx.EVT_BUTTON, self.multi)
        self.four.Bind(wx.EVT_BUTTON, self.number_input_four)
        self.five.Bind(wx.EVT_BUTTON, self.number_input_five)
        self.six.Bind(wx.EVT_BUTTON, self.number_input_six)
        self.minus.Bind(wx.EVT_BUTTON, self.substract)
        self.one.Bind(wx.EVT_BUTTON, self.number_input_one)
        self.two.Bind(wx.EVT_BUTTON, self.number_input_two)
        self.three.Bind(wx.EVT_BUTTON, self.number_input_three)
        self.plus.Bind(wx.EVT_BUTTON, self.addition)
        self.zero.Bind(wx.EVT_BUTTON, self.number_input_zero)
        self.decimal.Bind(wx.EVT_BUTTON, self.decmal)
        self.equal.Bind(wx.EVT_BUTTON, self.evaluate)

    def clear(self, event):
        self.text_history.SetValue(str(''))
        self.text.SetValue(str(''))

    def evaluate(self, event):
        """
        evaluate function finds the value of text which has been modified by different functions

        :param event: OnButtonClick section of calculator_gui\calc.fbp
        :return: evaluated **text**
        """
        try:
            self.text_history.SetValue(str(self.text.GetValue())+str(' ='))
            self.text.SetValue(str(eval(self.text.GetValue())))
        except Exception:
            print("Error in evaluating")

    # other buttons
    def multi(self, event):
        self.text.SetValue(str(self.text.GetValue())+str('*'))

    def divide(self, event):
        self.text.SetValue(str(float(self.text.GetValue()))+str('/'))

    def addition(self, event):
        self.text.SetValue(str(self.text.GetValue())+str('+'))

    def substract(self, event):
        self.text.SetValue(str(self.text.GetValue())+str('-'))

    def decmal(self, event):
        self.text.SetValue(str(self.text.GetValue()) + str('.'))

    def delete_char_from_right(self, event):
        current_string = str(self.text.GetValue())
        self.text.SetValue(current_string[:len(current_string)-1])

    def square_root(self, event):
        self.text.SetValue(str(math.sqrt(float(self.text.GetValue()))))

    def num_power(self, event):
        self.text.SetValue(str(self.text.GetValue()) + str('**'))

    def num_by_rev(self,event):
        try:
            _value = str('1')+str('/')+str(float(str(self.text.GetValue())))
            self.text.SetValue(str(eval(_value)))
        except Exception:
            print("Error in evaluating")

    def num_per(self, event):
        _value = float(self.text.GetValue())/100
        self.text.SetValue(str(_value))

    def num_factorial(self, event):
        _value = math.gamma(float(self.text.GetValue()))
        self.text_history.SetValue(str(self.text.GetValue())+str('!'))
        self.text.SetValue(str(_value))
    #number input from 0-9
    def number_input_zero(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(0))
        else:
            self.text.SetValue(str(self.text.GetValue())+str(0))

    def number_input_one(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(1))
        else:
            self.text.SetValue(str(self.text.GetValue())+str(1))

    def number_input_two(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(2))
        else:
            self.text.SetValue(str(self.text.GetValue())+str(2))

    def number_input_three(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(3))
        else:
            self.text.SetValue(str(self.text.GetValue())+str(3))

    def number_input_four(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(4))
        else:
            self.text.SetValue(str(self.text.GetValue())+str(4))

    def number_input_five(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(5))
        else:
            self.text.SetValue(str(self.text.GetValue())+str(5))

    def number_input_six( self, event ):
        if not self.text.GetValue():
            self.text.SetValue(str(6))
        else:
            self.text.SetValue(str(self.text.GetValue())+str(6))

    def number_input_seven( self, event ):
        if not self.text.GetValue():
            self.text.SetValue(str(7))
        else:
            self.text.SetValue(str(self.text.GetValue())+str(7))

    def number_input_eight( self, event ):
        if not self.text.GetValue():
            self.text.SetValue(str(8))
        else:
            self.text.SetValue(str(self.text.GetValue())+str(8))

    def number_input_nine(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(9))
        else:
            self.text.SetValue(str(self.text.GetValue()) + str(9))

if __name__ == "__main__":
    app = wx.App(False) # mandatory in wx, create an app, False stands for not deteriction stdin/stdout
    frame = CalcCall() # create an object of CalcFrame
    frame.Show(True) # show the frame
    app.MainLoop() # start the applications