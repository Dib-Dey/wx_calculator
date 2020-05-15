# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyPanel1
###########################################################################


class ClassicPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(600, 450),
                          style=wx.TAB_TRAVERSAL)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.text_history = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.text_history.SetFont(wx.Font(14, 74, 90, 90, False, "Arial"))

        bSizer1.Add(self.text_history, 0, wx.ALL | wx.EXPAND, 5)

        self.text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.text.SetFont(wx.Font(14, 74, 90, 90, False, "Arial"))

        bSizer1.Add(self.text, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.num_perc = wx.Button(self, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.num_perc.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.num_perc.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        self.num_perc.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer1.Add(self.num_perc, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.sqrt = wx.Button(self, wx.ID_ANY, u"sqrt", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.sqrt.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.sqrt.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        self.sqrt.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer1.Add(self.sqrt, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.x_power = wx.Button(self, wx.ID_ANY, u"xⁿ", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.x_power.SetDefault()
        self.x_power.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.x_power.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        self.x_power.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer1.Add(self.x_power, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.num_rev = wx.Button(self, wx.ID_ANY, u"1/x", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.num_rev.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.num_rev.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        self.num_rev.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer1.Add(self.num_rev, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(gbSizer1, 1, wx.ALL | wx.EXPAND, 5)

        gbSizer3 = wx.GridBagSizer(0, 0)
        gbSizer3.SetFlexibleDirection(wx.BOTH)
        gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Clear_Entry = wx.Button(self, wx.ID_ANY, u"x!", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.Clear_Entry.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.Clear_Entry.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer3.Add(self.Clear_Entry, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.clean = wx.Button(self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.clean.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.clean.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer3.Add(self.clean, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"«", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.m_button12.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button12.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer3.Add(self.m_button12, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_button13 = wx.Button(self, wx.ID_ANY, u"÷", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.m_button13.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button13.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer3.Add(self.m_button13, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(gbSizer3, 1, wx.ALL | wx.EXPAND, 5)

        gbSizer4 = wx.GridBagSizer(0, 0)
        gbSizer4.SetFlexibleDirection(wx.BOTH)
        gbSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.seven = wx.Button(self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.seven.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.seven.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        gbSizer4.Add(self.seven, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.eigth = wx.Button(self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize,
                               wx.NO_BORDER | wx.STATIC_BORDER)
        self.eigth.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.eigth.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        self.eigth.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        gbSizer4.Add(self.eigth, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.nine = wx.Button(self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.nine.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.nine.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        gbSizer4.Add(self.nine, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.multiply = wx.Button(self, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.multiply.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.multiply.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer4.Add(self.multiply, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(gbSizer4, 1, wx.ALL | wx.EXPAND, 5)

        gbSizer41 = wx.GridBagSizer(0, 0)
        gbSizer41.SetFlexibleDirection(wx.BOTH)
        gbSizer41.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.four = wx.Button(self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.four.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.four.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        gbSizer41.Add(self.four, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.five = wx.Button(self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.five.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.five.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        gbSizer41.Add(self.five, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.six = wx.Button(self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.six.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.six.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        gbSizer41.Add(self.six, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.minus = wx.Button(self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.minus.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.minus.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer41.Add(self.minus, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(gbSizer41, 1, wx.ALL | wx.EXPAND, 5)

        gbSizer5 = wx.GridBagSizer(0, 0)
        gbSizer5.SetFlexibleDirection(wx.BOTH)
        gbSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.one = wx.Button(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.one.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.one.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        gbSizer5.Add(self.one, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.two = wx.Button(self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.two.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.two.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        gbSizer5.Add(self.two, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.three = wx.Button(self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.three.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.three.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        gbSizer5.Add(self.three, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.plus = wx.Button(self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.plus.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.plus.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer5.Add(self.plus, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(gbSizer5, 1, wx.ALL | wx.EXPAND, 5)

        gbSizer6 = wx.GridBagSizer(0, 0)
        gbSizer6.SetFlexibleDirection(wx.BOTH)
        gbSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_button30 = wx.Button(self, wx.ID_ANY, u"±", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.m_button30.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button30.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer6.Add(self.m_button30, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.zero = wx.Button(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.zero.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.zero.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        gbSizer6.Add(self.zero, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.decimal = wx.Button(self, wx.ID_ANY, u".", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.decimal.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.decimal.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        gbSizer6.Add(self.decimal, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.equal = wx.Button(self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.equal.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.equal.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer6.Add(self.equal, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(gbSizer6, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

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

    def __del__(self):
        pass

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
            self.text_history.SetValue(str(self.text.GetValue()) + str(' ='))
            self.text.SetValue(str(eval(self.text.GetValue())))
        except Exception:
            print("Error in evaluating")

    # other buttons
    def multi(self, event):
        self.text.SetValue(str(self.text.GetValue()) + str('*'))

    def divide(self, event):
        self.text.SetValue(str(float(self.text.GetValue())) + str('/'))

    def addition(self, event):
        self.text.SetValue(str(self.text.GetValue()) + str('+'))

    def substract(self, event):
        self.text.SetValue(str(self.text.GetValue()) + str('-'))

    def decmal(self, event):
        self.text.SetValue(str(self.text.GetValue()) + str('.'))

    def delete_char_from_right(self, event):
        current_string = str(self.text.GetValue())
        self.text.SetValue(current_string[:len(current_string) - 1])

    def square_root(self, event):
        self.text.SetValue(str(math.sqrt(float(self.text.GetValue()))))

    def num_power(self, event):
        self.text.SetValue(str(self.text.GetValue()) + str('**'))

    def num_by_rev(self, event):
        try:
            _value = str('1') + str('/') + str(float(str(self.text.GetValue())))
            self.text.SetValue(str(eval(_value)))
        except Exception:
            print("Error in evaluating")

    def num_per(self, event):
        _value = float(self.text.GetValue()) / 100
        self.text.SetValue(str(_value))

    def num_factorial(self, event):
        _value = math.gamma(float(self.text.GetValue()))
        self.text_history.SetValue(str(self.text.GetValue()) + str('!'))
        self.text.SetValue(str(_value))

    # number input from 0-9
    def number_input_zero(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(0))
        else:
            self.text.SetValue(str(self.text.GetValue()) + str(0))

    def number_input_one(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(1))
        else:
            self.text.SetValue(str(self.text.GetValue()) + str(1))

    def number_input_two(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(2))
        else:
            self.text.SetValue(str(self.text.GetValue()) + str(2))

    def number_input_three(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(3))
        else:
            self.text.SetValue(str(self.text.GetValue()) + str(3))

    def number_input_four(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(4))
        else:
            self.text.SetValue(str(self.text.GetValue()) + str(4))

    def number_input_five(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(5))
        else:
            self.text.SetValue(str(self.text.GetValue()) + str(5))

    def number_input_six(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(6))
        else:
            self.text.SetValue(str(self.text.GetValue()) + str(6))

    def number_input_seven(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(7))
        else:
            self.text.SetValue(str(self.text.GetValue()) + str(7))

    def number_input_eight(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(8))
        else:
            self.text.SetValue(str(self.text.GetValue()) + str(8))

    def number_input_nine(self, event):
        if not self.text.GetValue():
            self.text.SetValue(str(9))
        else:
            self.text.SetValue(str(self.text.GetValue()) + str(9))

if __name__ == '__main__':
    app = wx.App()
    MainFrame = wx.Frame(None, title = "Calculator_Panel_test",size = (600,500))
    panel = ClassicPanel(MainFrame)
    MainFrame.Show(True)
    app.MainLoop()