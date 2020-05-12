# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import menubar
###########################################################################
## Class MyFrame
###########################################################################

class MyFrame( wx.Frame):
	def __init__(self, parent=None):
		super().__init__(parent,
					    id = wx.ID_ANY,
					    title = wx.EmptyString,
					    pos = wx.DefaultPosition,
					    size = wx.Size( 419,393 ),
					    style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
		self.SetMenuBar(self.CreateMenuBar())
		#MainFrame.__init__(self,parent)
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		# panel = wx.Panel(self, -1)# Panel(self, -1)
		# self.useredited = False
		# self.hassettingpanel = False
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
		self.num_perc.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.num_perc.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
		self.num_perc.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		gbSizer1.Add(self.num_perc, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

		self.sqrt = wx.Button(self, wx.ID_ANY, u"sqrt", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.sqrt.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.sqrt.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
		self.sqrt.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		gbSizer1.Add(self.sqrt, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

		self.x_power = wx.Button(self, wx.ID_ANY, u"xⁿ", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.x_power.SetDefault()
		self.x_power.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.x_power.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
		self.x_power.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		gbSizer1.Add(self.x_power, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

		self.num_rev = wx.Button(self, wx.ID_ANY, u"1/x", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.num_rev.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.num_rev.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
		self.num_rev.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		gbSizer1.Add(self.num_rev, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

		bSizer1.Add(gbSizer1, 1, wx.EXPAND, 5)

		gbSizer3 = wx.GridBagSizer(0, 0)
		gbSizer3.SetFlexibleDirection(wx.BOTH)
		gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.Clear_Entry = wx.Button(self, wx.ID_ANY, u"x!", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.Clear_Entry.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.Clear_Entry.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		gbSizer3.Add(self.Clear_Entry, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

		self.clean = wx.Button(self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.clean.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.clean.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		gbSizer3.Add(self.clean, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

		self.m_button12 = wx.Button(self, wx.ID_ANY, u"«", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.m_button12.SetFont(wx.Font(14, 74, 90, 90, False, "Arial"))
		self.m_button12.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		gbSizer3.Add(self.m_button12, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

		self.m_button13 = wx.Button(self, wx.ID_ANY, u"÷", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.m_button13.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.m_button13.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		gbSizer3.Add(self.m_button13, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

		bSizer1.Add(gbSizer3, 1, wx.EXPAND, 5)

		gbSizer4 = wx.GridBagSizer(0, 0)
		gbSizer4.SetFlexibleDirection(wx.BOTH)
		gbSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.seven = wx.Button(self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.seven.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.seven.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

		gbSizer4.Add(self.seven, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

		self.eigth = wx.Button(self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.eigth.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.eigth.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

		gbSizer4.Add(self.eigth, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

		self.nine = wx.Button(self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.nine.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.nine.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

		gbSizer4.Add(self.nine, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

		self.multiply = wx.Button(self, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.multiply.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.multiply.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		gbSizer4.Add(self.multiply, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

		bSizer1.Add(gbSizer4, 1, wx.EXPAND, 5)

		gbSizer41 = wx.GridBagSizer(0, 0)
		gbSizer41.SetFlexibleDirection(wx.BOTH)
		gbSizer41.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.four = wx.Button(self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.four.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.four.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

		gbSizer41.Add(self.four, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

		self.five = wx.Button(self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.five.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.five.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

		gbSizer41.Add(self.five, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

		self.six = wx.Button(self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.six.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.six.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

		gbSizer41.Add(self.six, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

		self.minus = wx.Button(self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.minus.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.minus.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		gbSizer41.Add(self.minus, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

		bSizer1.Add(gbSizer41, 1, wx.EXPAND, 5)

		gbSizer5 = wx.GridBagSizer(0, 0)
		gbSizer5.SetFlexibleDirection(wx.BOTH)
		gbSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.one = wx.Button(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.one.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.one.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

		gbSizer5.Add(self.one, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

		self.two = wx.Button(self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.two.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.two.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

		gbSizer5.Add(self.two, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

		self.three = wx.Button(self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.three.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.three.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

		gbSizer5.Add(self.three, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

		self.plus = wx.Button(self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.plus.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.plus.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		gbSizer5.Add(self.plus, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

		bSizer1.Add(gbSizer5, 1, wx.EXPAND, 5)

		gbSizer6 = wx.GridBagSizer(0, 0)
		gbSizer6.SetFlexibleDirection(wx.BOTH)
		gbSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_button30 = wx.Button(self, wx.ID_ANY, u"±", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.m_button30.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.m_button30.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		gbSizer6.Add(self.m_button30, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

		self.zero = wx.Button(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.zero.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.zero.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

		gbSizer6.Add(self.zero, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

		self.decimal = wx.Button(self, wx.ID_ANY, u".", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.decimal.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

		gbSizer6.Add(self.decimal, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

		self.equal = wx.Button(self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.equal.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
		self.equal.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		gbSizer6.Add(self.equal, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

		bSizer1.Add(gbSizer6, 1, wx.EXPAND, 5)

		self.SetSizer(bSizer1)
		self.Layout()

		self.Centre(wx.BOTH)



	def CreateMenuBar(self, with_window=False):
		# Make a menubar
		file_menu = wx.Menu()
		FPBTEST_QUIT = wx.NewIdRef()
		FPBTEST_REFRESH = wx.NewIdRef()
		FPB_BOTTOM_FOLD = wx.NewIdRef()
		FPB_SINGLE_FOLD = wx.NewIdRef()
		FPB_EXCLUSIVE_FOLD = wx.NewIdRef()
		FPBTEST_TOGGLE_WINDOW = wx.NewIdRef()
		FPBTEST_ABOUT = wx.NewIdRef()

		file_menu.Append(FPBTEST_QUIT, "&Exit")

		option_menu = None

		if with_window:
			# Dummy option
			option_menu = wx.Menu()
			option_menu.Append(FPBTEST_REFRESH, "&Refresh picture")

		# make fold panel menu

		fpb_menu = wx.Menu()
		fpb_menu.AppendCheckItem(FPB_BOTTOM_FOLD, "Create with &fpb.FPB_COLLAPSE_TO_BOTTOM")

		# Now Implemented!
		fpb_menu.AppendCheckItem(FPB_SINGLE_FOLD, "Create with &fpb.FPB_SINGLE_FOLD")

		# Now Implemented!
		fpb_menu.AppendCheckItem(FPB_EXCLUSIVE_FOLD, "Create with &fpb.FPB_EXCLUSIVE_FOLD")

		fpb_menu.AppendSeparator()
		fpb_menu.Append(FPBTEST_TOGGLE_WINDOW, "&Toggle FoldPanelBar")

		help_menu = wx.Menu()
		help_menu.Append(FPBTEST_ABOUT, "&About")

		menu_bar = wx.MenuBar()

		menu_bar.Append(file_menu, "&File")
		menu_bar.Append(fpb_menu, "&FoldPanel")

		if option_menu:
			menu_bar.Append(option_menu, "&Options")

		menu_bar.Append(help_menu, "&Help")

		# self.Bind(wx.EVT_MENU, self.OnAbout, id=FPBTEST_ABOUT)
		# self.Bind(wx.EVT_MENU, self.OnQuit, id=FPBTEST_QUIT)
		# self.Bind(wx.EVT_MENU, self.OnToggleWindow, id=FPBTEST_TOGGLE_WINDOW)
		# self.Bind(wx.EVT_MENU, self.OnCreateBottomStyle, id=FPB_BOTTOM_FOLD)
		# self.Bind(wx.EVT_MENU, self.OnCreateNormalStyle, id=FPB_SINGLE_FOLD)
		# self.Bind(wx.EVT_MENU, self.OnCreateExclusiveStyle, id=FPB_EXCLUSIVE_FOLD)
		#
		# self._bottomstyle = FPB_BOTTOM_FOLD
		# self._singlestyle = FPB_SINGLE_FOLD
		# self._exclusivestyle = FPB_EXCLUSIVE_FOLD

		return menu_bar


if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame()
	frame.Show(True)
	app.MainLoop()
