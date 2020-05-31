# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import function_factory
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

        self.factorial_ = wx.Button(self, wx.ID_ANY, u"x!", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.factorial_.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.factorial_.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer3.Add(self.factorial_, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

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
        self.clean.Bind(wx.EVT_BUTTON,
                        lambda event, text_history=self.text_history, text=self.text: function_factory.clear(event,
                                                                                                             text_history,
                                                                                                             text))
        # Note: Example of passing arguements to callback --> https://wiki.wxpython.org/Passing%20Arguments%20to%20Callbacks
        # self.clean.Bind(wx.EVT_BUTTON, function_factory.clear) #wx will always pass one argument to these functions - the event. You can extract current object --> "Self" by applying GetEventObject() on Event
        # self.clean.Bind(wx.EVT_BUTTON, self.clear)
        self.equal.Bind(wx.EVT_BUTTON, lambda event, text_history=self.text_history, text=self.text: function_factory.evaluate(event,
                                                                                                             text_history,
                                                                                                             text))
        self.factorial_.Bind(wx.EVT_BUTTON, lambda event, text_history=self.text_history, text=self.text: function_factory.num_factorial(event,
                                                                                                             text_history,
                                                                                                             text))
        self.num_perc.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.num_per(event, text))
        self.sqrt.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.square_root(event, text))
        self.x_power.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.num_power(event, text))
        self.num_rev.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.num_by_rev(event, text))
        self.m_button12.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.delete_char_from_right(event, text))
        self.m_button13.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.divide(event, text))
        self.seven.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.number_input_seven(event, text))
        self.eigth.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.number_input_eight(event, text))
        self.nine.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.number_input_nine(event, text))
        self.multiply.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.multi(event, text))
        self.four.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.number_input_four(event, text))
        self.five.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.number_input_five(event, text))
        self.six.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.number_input_six(event, text))
        self.minus.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.substract(event, text))
        self.one.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.number_input_one(event, text))
        self.two.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.number_input_two(event, text))
        self.three.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.number_input_three(event, text))
        self.plus.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.addition(event, text))
        self.zero.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.number_input_zero(event, text))
        self.decimal.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.decmal(event, text))

    def __del__(self):
        pass

    # other buttons

if __name__ == '__main__':
    app = wx.App()
    MainFrame = wx.Frame(None, title = "Calculator_Panel_test",size = (600,500))
    panel = ClassicPanel(MainFrame)
    MainFrame.Show(True)
    app.MainLoop()