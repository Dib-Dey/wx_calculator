###########################################################################

import wx
import wx.xrc
import function_factory


###########################################################################
## Class SciPanel
###########################################################################

class SciPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(600, 450),
                          style=wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)
        #Default radio button
        self.radio_button = 'DEC'

        # Formation of the GUI widgets
        bSizerP = wx.BoxSizer(wx.VERTICAL)

        self.text_history = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_RIGHT | wx.NO_BORDER)
        self.text_history.SetFont(wx.Font(9, 74, 90, 90, False, "Arial"))
        self.text_history.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizerP.Add(self.text_history, 0, wx.ALL | wx.EXPAND, 5)

        self.text = wx.TextCtrl(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT)
        self.text.SetFont(wx.Font(14, 74, 90, 90, False, "Arial"))
        bSizerP.Add(self.text, 0, wx.ALL | wx.EXPAND, 5)

        hex_box = wx.BoxSizer(wx.HORIZONTAL)

        self.hex_rb = wx.RadioButton(self, wx.ID_ANY, u"HEX", wx.DefaultPosition, wx.DefaultSize, 0)
        self.hex_rb.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        hex_box.Add(self.hex_rb, 0, wx.ALL, 5)

        self.hex_val = wx.TextCtrl(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize,
                                   0 | wx.NO_BORDER)
        self.hex_val.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        self.hex_val.SetFont(wx.Font(14, 74, 90, 90, False, "Arial"))
        hex_box.Add(self.hex_val, 1, wx.ALL, 0)

        bSizerP.Add(hex_box, 0, wx.EXPAND, 5)

        dec_box = wx.BoxSizer(wx.HORIZONTAL)

        self.dec_rb = wx.RadioButton(self, wx.ID_ANY, u"DEC", wx.DefaultPosition, wx.DefaultSize, 0)
        self.dec_rb.SetValue(True)
        self.dec_rb.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        dec_box.Add(self.dec_rb, 0, wx.ALL, 5)

        self.dec_val = wx.TextCtrl(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize,
                                   0 | wx.NO_BORDER)
        self.dec_val.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        self.dec_val.SetFont(wx.Font(14, 74, 90, 90, False, "Arial"))
        dec_box.Add(self.dec_val, 1, wx.ALL, 0)

        bSizerP.Add(dec_box, 0, wx.EXPAND, 5)

        oct_box = wx.BoxSizer(wx.HORIZONTAL)

        self.oct_rb = wx.RadioButton(self, wx.ID_ANY, u"OCT", wx.DefaultPosition, wx.DefaultSize, 0)
        self.oct_rb.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        oct_box.Add(self.oct_rb, 0, wx.ALL, 5)

        self.oct_val = wx.TextCtrl(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize,
                                   0 | wx.NO_BORDER)
        self.oct_val.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        self.oct_val.SetFont(wx.Font(14, 74, 90, 90, False, "Arial"))
        oct_box.Add(self.oct_val, 1, wx.ALL, 0)

        bSizerP.Add(oct_box, 0, wx.EXPAND, 5)

        bin_box = wx.BoxSizer(wx.HORIZONTAL)

        self.bin_rb = wx.RadioButton(self, wx.ID_ANY, u"BIN", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bin_rb.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bin_box.Add(self.bin_rb, 0, wx.ALL, 5)

        self.bin_val = wx.TextCtrl(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize,
                                   0 | wx.NO_BORDER)
        self.bin_val.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        self.bin_val.SetFont(wx.Font(14, 74, 90, 90, False, "Arial"))
        bin_box.Add(self.bin_val, 1, wx.ALL, 0)

        bSizerP.Add(bin_box, 0, wx.EXPAND, 5)

        bSizerRow1 = wx.BoxSizer(wx.HORIZONTAL)

        self.Lsh_b = wx.Button(self, wx.ID_ANY, u"Lsh", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lsh_b.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.Lsh_b.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizerRow1.Add(self.Lsh_b, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.Rsh_b = wx.Button(self, wx.ID_ANY, u"Rsh", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Rsh_b.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.Rsh_b.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow1.Add(self.Rsh_b, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.Or_b = wx.Button(self, wx.ID_ANY, u"OR", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Or_b.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.Or_b.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow1.Add(self.Or_b, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.Xor_b = wx.Button(self, wx.ID_ANY, u"XOR", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Xor_b.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.Xor_b.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow1.Add(self.Xor_b, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.Not_b = wx.Button(self, wx.ID_ANY, u"NOT", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Not_b.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.Not_b.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow1.Add(self.Not_b, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.And_b = wx.Button(self, wx.ID_ANY, u"AND", wx.DefaultPosition, wx.DefaultSize, 0)
        self.And_b.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.And_b.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow1.Add(self.And_b, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(bSizerRow1, 0, wx.EXPAND, 5)

        bSizerRow2 = wx.BoxSizer(wx.HORIZONTAL)

        self.Lsh1 = wx.Button(self, wx.ID_ANY, u"↑", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lsh1.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.Lsh1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizerRow2.Add(self.Lsh1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button501 = wx.Button(self, wx.ID_ANY, u"MOD", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button501.SetFont(wx.Font(16, 74, 90, 90, False, "Arial"))
        self.m_button501.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow2.Add(self.m_button501, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button511 = wx.Button(self, wx.ID_ANY, u"CE", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button511.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button511.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow2.Add(self.m_button511, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_clear = wx.Button(self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_clear.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_clear.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow2.Add(self.button_clear, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button531 = wx.Button(self, wx.ID_ANY, u"DEL", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button531.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button531.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow2.Add(self.m_button531, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_div = wx.Button(self, wx.ID_ANY, u"÷", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_div.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_div.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow2.Add(self.button_div, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(bSizerRow2, 0, 0, 5)

        bSizerRow3 = wx.BoxSizer(wx.HORIZONTAL)

        self.A = wx.Button(self, wx.ID_ANY, u"A", wx.DefaultPosition, wx.DefaultSize, 0)
        self.A.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.A.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow3.Add(self.A, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.B = wx.Button(self, wx.ID_ANY, u"B", wx.DefaultPosition, wx.DefaultSize, 0)
        self.B.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.B.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow3.Add(self.B, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_7 = wx.Button(self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_7.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow3.Add(self.button_7, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_8 = wx.Button(self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_8.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow3.Add(self.button_8, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_9 = wx.Button(self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_9.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow3.Add(self.button_9, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_mul = wx.Button(self, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_mul.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_mul.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow3.Add(self.button_mul, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(bSizerRow3, 0, 0, 5)

        bSizerRow4 = wx.BoxSizer(wx.HORIZONTAL)

        self.C = wx.Button(self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0)
        self.C.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.C.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow4.Add(self.C, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.D = wx.Button(self, wx.ID_ANY, u"D", wx.DefaultPosition, wx.DefaultSize, 0)
        self.D.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.D.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow4.Add(self.D, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_6 = wx.Button(self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_6.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow4.Add(self.button_6, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_5 = wx.Button(self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_5.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow4.Add(self.button_5, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_4 = wx.Button(self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_4.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow4.Add(self.button_4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_sub = wx.Button(self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_sub.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_sub.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow4.Add(self.button_sub, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(bSizerRow4, 0, wx.EXPAND, 5)

        bSizerRow5 = wx.BoxSizer(wx.HORIZONTAL)

        self.E = wx.Button(self, wx.ID_ANY, u"E", wx.DefaultPosition, wx.DefaultSize, 0)
        self.E.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.E.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow5.Add(self.E, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.F = wx.Button(self, wx.ID_ANY, u"F", wx.DefaultPosition, wx.DefaultSize, 0)
        self.F.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.F.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow5.Add(self.F, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_1 = wx.Button(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_1.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow5.Add(self.button_1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_2 = wx.Button(self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_2.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow5.Add(self.button_2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_3 = wx.Button(self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_3.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow5.Add(self.button_3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_plus = wx.Button(self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_plus.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_plus.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow5.Add(self.button_plus, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(bSizerRow5, 0, wx.EXPAND, 5)

        bSizerRow6 = wx.BoxSizer(wx.HORIZONTAL)

        self.Lsh11111 = wx.Button(self, wx.ID_ANY, u"(", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lsh11111.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.Lsh11111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizerRow6.Add(self.Lsh11111, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button5011111 = wx.Button(self, wx.ID_ANY, u")", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5011111.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button5011111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow6.Add(self.m_button5011111, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button5111111 = wx.Button(self, wx.ID_ANY, u"±", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5111111.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button5111111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow6.Add(self.m_button5111111, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_0 = wx.Button(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_0.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_0.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        bSizerRow6.Add(self.button_0, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_dec = wx.Button(self, wx.ID_ANY, u".", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_dec.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_dec.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow6.Add(self.button_dec, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_equal = wx.Button(self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_equal.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_equal.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow6.Add(self.button_equal, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(bSizerRow6, 0, wx.EXPAND, 5)

        self.SetSizer(bSizerP)
        self.Layout()

        # Connect Events
        self.Bind(wx.EVT_RADIOBUTTON, self.GetRadioButtonLabel)
        # Evaluate button
        # self.button_equal.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.evaluate(event,
        #                                                                                                      text_history,
        #                                                                                                      text))
        # other buttons
        self.m_button531.Bind(wx.EVT_BUTTON,
                              lambda event, text=self.text: function_factory.delete_char_from_right(event, text))
        # Clear button
        self.button_clear.Bind(wx.EVT_BUTTON, self.clear)
        # number functions
        self.button_0.Bind(wx.EVT_BUTTON, self.number_input_zero)
        self.button_1.Bind(wx.EVT_BUTTON, self.number_input_one)
        self.button_2.Bind(wx.EVT_BUTTON, self.number_input_two)
        self.button_3.Bind(wx.EVT_BUTTON, self.number_input_three)
        self.button_4.Bind(wx.EVT_BUTTON, self.number_input_four)
        self.button_5.Bind(wx.EVT_BUTTON, self.number_input_five)
        self.button_6.Bind(wx.EVT_BUTTON, self.number_input_six)
        self.button_7.Bind(wx.EVT_BUTTON, self.number_input_seven)
        self.button_8.Bind(wx.EVT_BUTTON, self.number_input_eight)
        self.button_9.Bind(wx.EVT_BUTTON, self.number_input_nine)

        # symbol functions
        self.Lsh_b.Bind(wx.EVT_BUTTON,self.left_shift)
        # self.button_div.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.divide(event, text))
        # self.button_sub.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.multi(event, text))
        # self.button_mul.Bind(wx.EVT_BUTTON, lambda event, text=self.text: function_factory.substract(event, text))
        # self.button_plus.Bind(wx.EVT_BUTTON,
        # self.button_dec.Bind(wx.EVT_BUTTON,
        #Evaluate
        self.button_equal.Bind(wx.EVT_BUTTON,self.evaluate)

    def __del__(self):
        pass

    def left_shift(self, event):
        self.text_history.SetValue(self.text.GetValue() + "  Lsh")

    def evaluate(self):
        

    def GetRadioButtonLabel(self, event):
        """ Bind function for clicking any of the 4 radio button"""
        bin_disable_button = [self.button_2, self.button_3, self.button_4, self.button_5, self.button_6, self.button_7,
                              self.button_8, self.button_9, self.A, self.B, self.C, self.D, self.E, self.F]
        dec_disable_button = [self.A, self.B, self.C, self.D, self.E, self.F]
        oct_disable_button = [self.button_8, self.button_9, self.A, self.B, self.C, self.D, self.E, self.F]
        rb = event.GetEventObject()
        print(f'{rb.GetLabel()} and {type(rb.GetLabel())} is clicked from Radio Group')
        self.radio_button = rb.GetLabel()
        if self.radio_button == 'DEC':
            self.text.SetValue(self.dec_val.GetValue())
            for item in bin_disable_button:
                item.Enable()
            for item in dec_disable_button:
                item.Disable()
            self.text.SetValue(self.text.GetValue())
        if self.radio_button == 'HEX':
            self.text.SetValue(self.hex_val.GetValue())
            for item in bin_disable_button:
                item.Enable()
        if self.radio_button == 'OCT':
            self.text.SetValue(self.oct_val.GetValue())
            for item in bin_disable_button:
                item.Enable()
            for item in oct_disable_button:
                item.Disable()
        if self.radio_button == 'BIN':
            self.text.SetValue(self.bin_val.GetValue())
            for item in bin_disable_button:
                item.Disable()

    def clear(self, event):
        self.text.SetValue('0')
        self.text_history.SetValue('')
        self.hex_val.SetValue('0')
        self.dec_val.SetValue('0')
        self.oct_val.SetValue('0')
        self.bin_val.SetValue('0')

    def check_text(func):
        def wrapper(self, input):
            if not self.text_history.GetValue():
                if self.text.GetValue() == '0':
                    self.text.SetValue('')
                func(self, input)
            else:
                self.text_history.SetValue(self.text_history.GetValue() + " " + input)

        return wrapper

    def number_input_zero(self, event):
        self.eval_every_button('0')

    def number_input_one(self, event):
        self.eval_every_button('1')
   
    def number_input_two(self, event):
        self.eval_every_button('2')
   
    def number_input_three(self, event):
        self.eval_every_button('3')
   
    def number_input_four(self, event):
        self.eval_every_button('4')

    def number_input_five(self, event):
        self.eval_every_button('5')
   
    def number_input_six(self, event):
        self.eval_every_button('6')

    def number_input_seven(self, event):
        self.eval_every_button('7')
   
    def number_input_eight(self, event):
        self.eval_every_button('8')

    def number_input_nine(self, event):
        self.eval_every_button('9')

    @check_text
    def eval_every_button(self, input):
        self.text.SetValue(self.text.GetValue() + input)
        if self.radio_button == 'DEC':
            self.dec_val.SetValue(self.text.GetValue())
            self.hex_val.SetValue(hex(eval(self.text.GetValue().lstrip('0'))))
            self.oct_val.SetValue(oct(eval(self.text.GetValue().lstrip('0'))))
            self.bin_val.SetValue(bin(eval(self.text.GetValue().lstrip('0'))))
        if self.radio_button == 'HEX':
            self.hex_val.SetValue(self.text.GetValue())
            self.dec_val.SetValue(str(int(self.text.GetValue(), 16)))
            self.oct_val.SetValue(oct(int(self.text.GetValue(), 16)))
            self.bin_val.SetValue(bin(int(self.text.GetValue(), 16)))
        if self.radio_button == 'OCT':
            self.oct_val.SetValue(self.text.GetValue())
            self.dec_val.SetValue(str(int(self.text.GetValue(), 8)))
            self.hex_val.SetValue(hex(int(self.text.GetValue(), 8)))
            self.bin_val.SetValue(bin(int(self.text.GetValue(), 8)))
        if self.radio_button == 'BIN':
            self.bin_val.SetValue(self.text.GetValue())
            self.dec_val.SetValue(str(int(self.text.GetValue(), 2)))
            self.oct_val.SetValue(oct(int(self.text.GetValue(), 2)))
            self.hex_val.SetValue(hex(int(self.text.GetValue(), 2)))
