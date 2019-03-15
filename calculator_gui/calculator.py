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
from math import *
class CalcFrame(gui.MyFrame):
    # constructor
    def __init__(self):
        # initialize parent class
        gui.MyFrame.__init__(self, parent=None)

    def clear(self, event):
        self.text.SetValue('')

    def evaluate(self, event):
        """
        evaluate function finds the value of text which has been modified by different functions

        :param event: OnButtonClick section of calculator_gui\calc.fbp
        :return: evaluated **text**
        """
        try:
            self.text.SetValue(str(eval(self.text.GetValue())))
        except Exception:
            print "Error in evaluating"

    def multi(self, event):
        self.text.SetValue(str(self.text.GetValue())+str('*'))

    def divide(self, event):
        self.text.SetValue(str(self.text.GetValue())+str('/'))

    def addition(self, event):
        self.text.SetValue(str(self.text.GetValue())+str('+'))

    def substract(self, event):
        self.text.SetValue(str(self.text.GetValue())+str('-'))

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
            self.text.SetValue(str())
        else:
            self.text.SetValue(str(self.text.GetValue()) + str(9))

    def radbuttom(self, event):
        print self.text.get_value()
        return 10

    def inv(self, event):
        ans = eval(self.text.GetValue())
        self.text.SetValue(str(ans))

    def pi_generator(self, event):
            self.text.SetValue(str(pi))

    # put a blank string in text when 'Clear' is clicked
    def clearFunc(self, event):
        self.text.SetValue(str(''))

if __name__ == "__main__":
    app = wx.App(False) # mandatory in wx, create an app, False stands for not deteriction stdin/stdout
    frame = CalcFrame() # create an object of CalcFrame
    frame.Show(True) # show the frame
    app.MainLoop() # start the applications