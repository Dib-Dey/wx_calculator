###########################################################################

import wx
import wx.xrc
import function_factory
import functools
###########################################################################
## Class ProgPanel
###########################################################################

class ProgPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(600, 450),
                          style=wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)
        #Default variables
        self.radio_button = 'DEC'
        self.eval_tracker = ""

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
        #Button Lsh and Rsh are here. WHich will be visible and can be switched to Rol and Lol
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

        self.b_switch = wx.Button(self, wx.ID_ANY, u"↑", wx.DefaultPosition, wx.DefaultSize, 0)
        self.b_switch.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.b_switch.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizerRow2.Add(self.b_switch, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_mod = wx.Button(self, wx.ID_ANY, u"MOD", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_mod.SetFont(wx.Font(16, 74, 90, 90, False, "Arial"))
        self.button_mod.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow2.Add(self.button_mod, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_ce = wx.Button(self, wx.ID_ANY, u"CE", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_ce.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_ce.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow2.Add(self.button_ce, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_clear = wx.Button(self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_clear.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_clear.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow2.Add(self.button_clear, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_del_from_right = wx.Button(self, wx.ID_ANY, u"DEL", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_del_from_right.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_del_from_right.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow2.Add(self.button_del_from_right, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_div = wx.Button(self, wx.ID_ANY, u"÷", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_div.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_div.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow2.Add(self.button_div, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(bSizerRow2, 0, 0, 5)

        bSizerRow3 = wx.BoxSizer(wx.HORIZONTAL)

        self.button_A = wx.Button(self, wx.ID_ANY, u"A", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_A.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_A.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow3.Add(self.button_A, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)
        self.button_A.Disable()

        self.button_B = wx.Button(self, wx.ID_ANY, u"B", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_B.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_B.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow3.Add(self.button_B, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)
        self.button_B.Disable()

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

        self.button_C = wx.Button(self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_C.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_C.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow4.Add(self.button_C, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)
        self.button_C.Disable()

        self.button_D = wx.Button(self, wx.ID_ANY, u"D", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_D.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_D.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow4.Add(self.button_D, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)
        self.button_D.Disable()

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

        self.button_E = wx.Button(self, wx.ID_ANY, u"E", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_E.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_E.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow5.Add(self.button_E, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)
        self.button_E.Disable()

        self.button_F = wx.Button(self, wx.ID_ANY, u"F", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_F.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_F.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow5.Add(self.button_F, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)
        self.button_F.Disable()

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

        self.b_left_bracket = wx.Button(self, wx.ID_ANY, u"(", wx.DefaultPosition, wx.DefaultSize, 0)
        self.b_left_bracket.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.b_left_bracket.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizerRow6.Add(self.b_left_bracket, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.b_right_bracket = wx.Button(self, wx.ID_ANY, u")", wx.DefaultPosition, wx.DefaultSize, 0)
        self.b_right_bracket.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.b_right_bracket.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow6.Add(self.b_right_bracket, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_plus_minus = wx.Button(self, wx.ID_ANY, u"±", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_plus_minus.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_plus_minus.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow6.Add(self.button_plus_minus, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_0 = wx.Button(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_0.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_0.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        bSizerRow6.Add(self.button_0, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_dec = wx.Button(self, wx.ID_ANY, u".", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_dec.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.button_dec.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

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

        # Clear button
        self.button_clear.Bind(wx.EVT_BUTTON, self.clear)
        self.button_ce.Bind(wx.EVT_BUTTON,self.clear_entry)
        # other buttons
        self.button_del_from_right.Bind(wx.EVT_BUTTON,self.delete_from_right)
        self.button_plus_minus.Bind(wx.EVT_BUTTON, self.plus_minus)
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
        #Hex Letter function
        self.button_A.Bind(wx.EVT_BUTTON,self.input_A)
        self.button_B.Bind(wx.EVT_BUTTON, self.input_B)
        self.button_C.Bind(wx.EVT_BUTTON, self.input_C)
        self.button_D.Bind(wx.EVT_BUTTON, self.input_D)
        self.button_E.Bind(wx.EVT_BUTTON, self.input_E)
        self.button_F.Bind(wx.EVT_BUTTON, self.input_F)
        # symbol functions
        self.Lsh_b.Bind(wx.EVT_BUTTON,self.left_shift)
        self.Rsh_b.Bind(wx.EVT_BUTTON,self.right_shift)
        self.Or_b.Bind(wx.EVT_BUTTON, self.or_func)
        self.Xor_b.Bind(wx.EVT_BUTTON, self.xor_func)
        self.Not_b.Bind(wx.EVT_BUTTON, self.not_func)
        self.And_b.Bind(wx.EVT_BUTTON, self.and_func)
        self.button_div.Bind(wx.EVT_BUTTON, self.divide)
        self.button_mul.Bind(wx.EVT_BUTTON, self.multi)
        self.button_sub.Bind(wx.EVT_BUTTON, self.substract)
        self.button_plus.Bind(wx.EVT_BUTTON, self.add)
        self.b_switch.Bind(wx.EVT_BUTTON, self.switch)
        self.button_mod.Bind(wx.EVT_BUTTON, self.mod_func)

        #Evaluate
        self.button_equal.Bind(wx.EVT_BUTTON,self.evaluate)
        self.b_left_bracket.Bind(wx.EVT_BUTTON,self.left_bracket)
        self.b_right_bracket.Bind(wx.EVT_BUTTON, self.right_bracket)
        self.button_dec.Bind(wx.EVT_BUTTON, self.dec_func)

    def __del__(self):
        pass

    def dec_func(self, event):
        pass

    def switch(self, event):
        if self.Lsh_b.GetLabel() == "Lsh":
            self.Lsh_b.SetLabel("LoL")
            self.Rsh_b.SetLabel("RoL")
        else:
            self.Lsh_b.SetLabel("Lsh")
            self.Rsh_b.SetLabel("Rsh")

    def GetRadioButtonLabel(self, event):
        """ Bind function for clicking any of the 4 radio button"""
        bin_disable_button = [self.button_dec, self.button_2, self.button_3, self.button_4, self.button_5, self.button_6, self.button_7,
                              self.button_8, self.button_9, self.button_A, self.button_B, self.button_C, self.button_D, self.button_E, self.button_F]
        dec_disable_button = [self.button_dec, self.button_A, self.button_B, self.button_C, self.button_D, self.button_E, self.button_F]
        oct_disable_button = [self.button_dec, self.button_8, self.button_9, self.button_A, self.button_B, self.button_C, self.button_D, self.button_E, self.button_F]
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

    def clear_entry(self, Event):
        self.text.SetValue('0')
        self.hex_val.SetValue('0')
        self.dec_val.SetValue('0')
        self.oct_val.SetValue('0')
        self.bin_val.SetValue('0')

    def delete_from_right(self,Event):
        try:
            _value_string = self.text.GetValue()
            _new_value_string = _value_string[0:len(_value_string)-1]
            if _new_value_string:
                self.text.SetValue(_new_value_string)
                self.eval_input("")
            else:
                self.clear(Event)
        except Exception as e:
            print(e)
            pass

    def plus_minus(self, Event):
        _value_string = self.text.GetValue()
        if _value_string[0] == "-":
            _new_value_string = _value_string.lstrip("-")
        else:
            _new_value_string = "-" + _value_string
        if _new_value_string:
            self.text.SetValue(_new_value_string)
            self.eval_input("")

    def input_special_operator_decorator(function):
        """
        Decorator for special operator like Lsh, Rsh, OR, XOR, NOR etc
        """
        def wrapper(self, event):
            if self.text.GetValue() != "0":
                self.text_history.SetValue(self.text_history.GetValue() + " " + self.text.GetValue())
                self.text.SetValue("")
            function(self, event)
        return wrapper

    def input_operator_decorator(function):
        """
        Decorator for any symbol like x, + , -, (, ), = etc...
        """
        @functools.wraps(function)
        def wrapper(self, event):
            if self.text.GetValue() != "0":
                self.text_history.SetValue(self.text_history.GetValue() + " " + self.text.GetValue())
            if self.text_history.GetValue():
                #print(f'Debug input_operator_decorator Info - {eval(self.text_history.GetValue())}')
                try:
                    self.text.SetValue(str(eval(self.text_history.GetValue())))
                    self.eval_tracker = str(eval(self.text_history.GetValue()))
                except:
                    self.eval_tracker = self.text.GetValue()
            function(self,event)
            #This line is to convert the self.text into oct/hex/bin/dec
            self.eval_input("")
        return wrapper

    def input_text_decorator(func):
        """
        Decorator to check whether text is clean/or in process of writing
        """
        @functools.wraps(func)
        def wrapper(self, input):
            print(f'Debug - input_text_decorator: eval_tracker - {self.eval_tracker}')
            if input:
                if self.text.GetValue() == "0" or self.eval_tracker == self.text.GetValue():
                    #tracker variable keep evaluating history. If it matches text, set to zero and add new string next
                    self.text.SetValue('')
                    self.eval_tracker = ''
                self.text.SetValue(self.text.GetValue() + input)
            func(self, input)
        return wrapper

    def input_A(self, Event):
        self.eval_input('A')

    def input_B(self, Event):
        self.eval_input('B')

    def input_C(self, Event):
        self.eval_input('C')

    def input_D(self, Event):
        self.eval_input('D')

    def input_E(self, Event):
        self.eval_input('E')

    def input_F(self, Event):
        self.eval_input('F')

    def number_input_zero(self, event):
        self.eval_input('0')

    def number_input_one(self, event):
        self.eval_input('1')

    def number_input_two(self, event):
        self.eval_input('2')

    def number_input_three(self, event):
        self.eval_input('3')

    def number_input_four(self, event):
        self.eval_input('4')

    def number_input_five(self, event):
        self.eval_input('5')

    def number_input_six(self, event):
        self.eval_input('6')

    def number_input_seven(self, event):
        self.eval_input('7')

    def number_input_eight(self, event):
        self.eval_input('8')

    def number_input_nine(self, event):
        self.eval_input('9')

    @input_operator_decorator
    def mod_func(self, event):
        self.text_history.SetValue(self.text_history.GetValue() + " %")

    def left_bracket(self,event):
        self.text_history.SetValue(self.text_history.GetValue() + " (")
        self.text.SetValue("")

    def right_bracket(self,event):
        self.text_history.SetValue(self.text_history.GetValue() + " " + self.text.GetValue())
        self.text_history.SetValue(self.text_history.GetValue() + " )")
        self.text.SetValue("")

    @input_operator_decorator
    def divide(self, event):
        "division function"
        self.text_history.SetValue(self.text_history.GetValue() + " //")

    @input_operator_decorator
    def substract(self, event):
        self.text_history.SetValue(self.text_history.GetValue() + " -")

    @input_operator_decorator
    def multi(self, event):
        self.text_history.SetValue(self.text_history.GetValue() + " *")

    @input_operator_decorator
    def add(self, event):
        self.text_history.SetValue(self.text_history.GetValue() + " +")

    @input_special_operator_decorator
    def left_shift(self, event):
        self.text_history.SetValue(self.dec_val.GetValue() + " Lsh")

    @input_special_operator_decorator
    def right_shift(self, event):
        self.text_history.SetValue(self.text.GetValue() + " Rsh")
        self.text.SetValue("")

    @input_special_operator_decorator
    def or_func(self, event):
        self.text_history.SetValue(self.dec_val.GetValue() + " OR")

    @input_special_operator_decorator
    def xor_func(self, event):
        self.text_history.SetValue(self.dec_val.GetValue() + " XOR")

    def not_func(self, event):
        self.text_history.SetValue(self.dec_val.GetValue() + " NOT")
        self.text.SetValue("Press Equal to Evaluate")

    @input_special_operator_decorator
    def and_func(self, event):
        self.text_history.SetValue(self.dec_val.GetValue() + " AND")

    @input_operator_decorator
    def evaluate(self, event):
        """
        It defines the characteristics of special function like Lsh, Rsh, XOR etc..
        """
        if self.text_history.GetValue():
            try:
                #try to evaluate history. It should be same as self.eval_tracker. Put tracker ""
                #print(f'Evaluate following : {eval(self.text_history.GetValue())}')
                self.text.SetValue(str(eval(self.text_history.GetValue())))
                self.eval_input("")
            except Exception as e:
                print(e)
                try:
                    _list = self.text_history.GetValue().split(" ")
                    _value = int(_list[0])
                    _factor = int(self.dec_val.GetValue())
                    if _list[1] == "Lsh":
                        for _ in range(int(_factor)):
                            _value = _value * 2
                    elif _list[1] == "Rsh":
                        for _ in range(int(_factor)):
                            _value = _value // 2
                    elif _list[1] == "OR":
                        _value = _value | _factor
                    elif _list[1] == "XOR":
                        _value = _value ^ _factor
                    elif _list[1] == "NOT":
                        _value = ~_value
                    elif _list[1] == "AND":
                        _value = _value & _factor
                    if self.radio_button == 'DEC':
                        self.text.SetValue(str(_value))
                    elif self.radio_button == 'HEX':
                        self.text.SetValue(hex(_value))
                    elif self.radio_button == 'OCT':
                        self.text.SetValue(oct(_value))
                    elif self.radio_button == 'BIN':
                        self.text.SetValue(bin(_value))
                    self.text.SetValue(str(_value))
                    self.eval_input("")
                except Exception as e:
                    print(e)
                    self.text.SetValue("ERROR")

    @input_text_decorator
    def eval_input(self, input):
        """
        input not given --> convert the text
        input given --> concatenate(decorator) the input to text and then convert the text
        Goal of this function is to get any input and depending on the button condition, convert it into hex/dec/oct/Bin
        """
        try:
            print(f"Debug - eval_input function try : eval_input {self.text.GetValue()}")
            _text_str = self.text.GetValue()
            _text_int = int(self.text.GetValue())
        except:
            pass
        if self.radio_button == 'DEC':
            self.dec_val.SetValue(_text_str)
            self.hex_val.SetValue(hex(_text_int))
            self.oct_val.SetValue(oct(_text_int))
            self.bin_val.SetValue(bin(_text_int))
        if self.radio_button == 'HEX':
            self.hex_val.SetValue(_text_str)
            self.dec_val.SetValue(str(int(_text_str, 16)))
            self.oct_val.SetValue(oct(int(_text_str, 16)))
            self.bin_val.SetValue(bin(int(_text_str, 16)))
        if self.radio_button == 'OCT':
            self.oct_val.SetValue(_text_str)
            self.dec_val.SetValue(str(int(_text_str, 8)))
            self.hex_val.SetValue(hex(int(_text_str, 8)))
            self.bin_val.SetValue(bin(int(_text_str, 8)))
        if self.radio_button == 'BIN':
            self.bin_val.SetValue(_text_str)
            self.dec_val.SetValue(str(int(_text_str, 2)))
            self.oct_val.SetValue(oct(int(_text_str, 2)))
            self.hex_val.SetValue(hex(int(_text_str, 2)))

if __name__ == '__main__':
    app=wx.App()
    frame =wx.Frame(None, title = "Calculator_Panel_test",size = (600,500))
    panel_test = ProgPanel(frame)
    frame.Show(True)
    app.MainLoop()