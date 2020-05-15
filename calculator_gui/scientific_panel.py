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
## Class SciPanel
###########################################################################
class SciPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(600, 450),
                          style=wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)

        bSizerP = wx.BoxSizer(wx.VERTICAL)

        self.Text_Show = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerP.Add(self.Text_Show, 0, wx.ALL | wx.EXPAND, 5)

        hex_box = wx.BoxSizer(wx.HORIZONTAL)

        self.hex_stat = wx.StaticText(self, wx.ID_ANY, u"HEX", wx.DefaultPosition, wx.DefaultSize, 0)
        self.hex_stat.Wrap(-1)
        self.hex_stat.SetFont(wx.Font(14, 74, 90, 92, False, "Arial"))

        hex_box.Add(self.hex_stat, 0, wx.ALL, 5)

        self.hex_value = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     0 | wx.NO_BORDER)
        self.hex_value.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        hex_box.Add(self.hex_value, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(hex_box, 0, wx.EXPAND, 5)

        dec_box = wx.BoxSizer(wx.HORIZONTAL)

        self.dec_val = wx.StaticText(self, wx.ID_ANY, u"DEC", wx.DefaultPosition, wx.DefaultSize, 0)
        self.dec_val.Wrap(-1)
        self.dec_val.SetFont(wx.Font(14, 74, 90, 92, False, "Arial"))

        dec_box.Add(self.dec_val, 0, wx.ALL, 5)

        self.dec_val = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   0 | wx.NO_BORDER)
        self.dec_val.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        dec_box.Add(self.dec_val, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(dec_box, 0, wx.EXPAND, 5)

        oct_box = wx.BoxSizer(wx.HORIZONTAL)

        self.oct_stat = wx.StaticText(self, wx.ID_ANY, u"OCT", wx.DefaultPosition, wx.DefaultSize, 0)
        self.oct_stat.Wrap(-1)
        self.oct_stat.SetFont(wx.Font(14, 74, 90, 92, False, "Arial"))

        oct_box.Add(self.oct_stat, 0, wx.ALL, 5)

        self.oct_val = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   0 | wx.NO_BORDER)
        self.oct_val.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        oct_box.Add(self.oct_val, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(oct_box, 0, wx.EXPAND, 5)

        bin_box = wx.BoxSizer(wx.HORIZONTAL)

        self.bin_stat = wx.StaticText(self, wx.ID_ANY, u"BIN", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bin_stat.Wrap(-1)
        self.bin_stat.SetFont(wx.Font(14, 74, 90, 92, False, "Arial"))

        bin_box.Add(self.bin_stat, 0, wx.ALL, 5)

        self.bin_box = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                   0 | wx.NO_BORDER)
        self.bin_box.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bin_box.Add(self.bin_box, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(bin_box, 0, wx.EXPAND, 0)

        bSizerRow1 = wx.BoxSizer(wx.HORIZONTAL)

        self.Lsh = wx.Button(self, wx.ID_ANY, u"Lsh", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lsh.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.Lsh.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizerRow1.Add(self.Lsh, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.Rsh = wx.Button(self, wx.ID_ANY, u"Rsh", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Rsh.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.Rsh.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow1.Add(self.Rsh, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.Or = wx.Button(self, wx.ID_ANY, u"OR", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Or.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.Or.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow1.Add(self.Or, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button52 = wx.Button(self, wx.ID_ANY, u"XOR", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button52.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button52.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow1.Add(self.m_button52, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button53 = wx.Button(self, wx.ID_ANY, u"NOT", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button53.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button53.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow1.Add(self.m_button53, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button54 = wx.Button(self, wx.ID_ANY, u"AND", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button54.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button54.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow1.Add(self.m_button54, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(bSizerRow1, 0, wx.EXPAND, 5)

        bSizerRow11 = wx.BoxSizer(wx.HORIZONTAL)

        self.Lsh1 = wx.Button(self, wx.ID_ANY, u"↑", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lsh1.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.Lsh1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizerRow11.Add(self.Lsh1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button501 = wx.Button(self, wx.ID_ANY, u"MOD", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button501.SetFont(wx.Font(16, 74, 90, 90, False, "Arial"))
        self.m_button501.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow11.Add(self.m_button501, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button511 = wx.Button(self, wx.ID_ANY, u"CE", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button511.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button511.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow11.Add(self.m_button511, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button521 = wx.Button(self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button521.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button521.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow11.Add(self.m_button521, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button531 = wx.Button(self, wx.ID_ANY, u"DEL", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button531.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button531.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow11.Add(self.m_button531, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button541 = wx.Button(self, wx.ID_ANY, u"÷", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button541.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button541.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow11.Add(self.m_button541, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(bSizerRow11, 0, 0, 5)

        bSizerRow111 = wx.BoxSizer(wx.HORIZONTAL)

        self.A = wx.Button(self, wx.ID_ANY, u"A", wx.DefaultPosition, wx.DefaultSize, 0)
        self.A.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.A.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow111.Add(self.A, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.B = wx.Button(self, wx.ID_ANY, u"B", wx.DefaultPosition, wx.DefaultSize, 0)
        self.B.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.B.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow111.Add(self.B, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_7 = wx.Button(self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_7.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow111.Add(self.button_7, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_8 = wx.Button(self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_8.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow111.Add(self.button_8, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_9 = wx.Button(self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_9.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow111.Add(self.button_9, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button5411 = wx.Button(self, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5411.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button5411.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow111.Add(self.m_button5411, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(bSizerRow111, 0, 0, 5)

        bSizerRow1111 = wx.BoxSizer(wx.HORIZONTAL)

        self.C = wx.Button(self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0)
        self.C.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.C.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow1111.Add(self.C, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.D = wx.Button(self, wx.ID_ANY, u"D", wx.DefaultPosition, wx.DefaultSize, 0)
        self.D.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.D.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow1111.Add(self.D, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_6 = wx.Button(self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_6.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow1111.Add(self.button_6, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_5 = wx.Button(self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_5.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow1111.Add(self.button_5, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_4 = wx.Button(self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_4.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow1111.Add(self.button_4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button54111 = wx.Button(self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button54111.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button54111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow1111.Add(self.m_button54111, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(bSizerRow1111, 0, wx.EXPAND, 5)

        bSizerRow11111 = wx.BoxSizer(wx.HORIZONTAL)

        self.E = wx.Button(self, wx.ID_ANY, u"E", wx.DefaultPosition, wx.DefaultSize, 0)
        self.E.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.E.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow11111.Add(self.E, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.F = wx.Button(self, wx.ID_ANY, u"F", wx.DefaultPosition, wx.DefaultSize, 0)
        self.F.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.F.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        bSizerRow11111.Add(self.F, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_1 = wx.Button(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_1.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow11111.Add(self.button_1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_2 = wx.Button(self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_2.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow11111.Add(self.button_2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_3 = wx.Button(self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_3.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))

        bSizerRow11111.Add(self.button_3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button541111 = wx.Button(self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button541111.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button541111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow11111.Add(self.m_button541111, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(bSizerRow11111, 0, wx.EXPAND, 5)

        bSizerRow111111 = wx.BoxSizer(wx.HORIZONTAL)

        self.Lsh11111 = wx.Button(self, wx.ID_ANY, u"(", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lsh11111.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.Lsh11111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizerRow111111.Add(self.Lsh11111, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button5011111 = wx.Button(self, wx.ID_ANY, u")", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5011111.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button5011111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow111111.Add(self.m_button5011111, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button5111111 = wx.Button(self, wx.ID_ANY, u"±", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5111111.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button5111111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow111111.Add(self.m_button5111111, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button5211111 = wx.Button(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5211111.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button5211111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        bSizerRow111111.Add(self.m_button5211111, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button5311111 = wx.Button(self, wx.ID_ANY, u".", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5311111.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button5311111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow111111.Add(self.m_button5311111, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_button5411111 = wx.Button(self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5411111.SetFont(wx.Font(18, 74, 90, 90, False, "Arial"))
        self.m_button5411111.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerRow111111.Add(self.m_button5411111, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizerP.Add(bSizerRow111111, 0, wx.EXPAND, 5)

        self.SetSizer(bSizerP)
        self.Layout()

    def __del__(self):
        pass


if __name__ == '__main__':
    app=wx.App()
    frame =wx.Frame(None, title = "Calculator_Panel_test",size = (600,500))
    panel_test = SciPanel(frame)
    frame.Show(True)
    app.MainLoop()