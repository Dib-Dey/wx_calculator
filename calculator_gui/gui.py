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
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 411,310 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.text, 0, wx.ALL|wx.EXPAND, 5 )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.percent = wx.Button( self, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.percent, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.sqrt = wx.Button( self, wx.ID_ANY, u"sqrt", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.sqrt, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.x_to_power_2 = wx.Button( self, wx.ID_ANY, u"x2", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.x_to_power_2, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.byx = wx.Button( self, wx.ID_ANY, u"1/x", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.byx, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer1.Add( gbSizer1, 1, wx.EXPAND, 5 )
		
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.Clear_Entry = wx.Button( self, wx.ID_ANY, u"CE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.Clear_Entry, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.clean = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.clean, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"«", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.m_button12, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button13 = wx.Button( self, wx.ID_ANY, u"÷", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.m_button13, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer1.Add( gbSizer3, 1, wx.EXPAND, 5 )
		
		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.seven = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.seven, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.eigth = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.eigth, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.nine = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.nine, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.multiply = wx.Button( self, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.multiply, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer1.Add( gbSizer4, 1, wx.EXPAND, 5 )
		
		gbSizer41 = wx.GridBagSizer( 0, 0 )
		gbSizer41.SetFlexibleDirection( wx.BOTH )
		gbSizer41.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.four = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer41.Add( self.four, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.five = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer41.Add( self.five, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.six = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer41.Add( self.six, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.minus = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer41.Add( self.minus, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer1.Add( gbSizer41, 1, wx.EXPAND, 5 )
		
		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.one = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.one, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.two = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.two, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.three = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.three, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.plus = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.plus, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer1.Add( gbSizer5, 1, wx.EXPAND, 5 )
		
		gbSizer6 = wx.GridBagSizer( 0, 0 )
		gbSizer6.SetFlexibleDirection( wx.BOTH )
		gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_button30 = wx.Button( self, wx.ID_ANY, u"±", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.m_button30, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.zero = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.zero, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.decimal = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.decimal, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.equal = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.equal, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer1.Add( gbSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.percent.Bind( wx.EVT_BUTTON, self.radbuttom )
		self.Clear_Entry.Bind( wx.EVT_BUTTON, self.inv )
		self.clean.Bind( wx.EVT_BUTTON, self.clear )
		self.seven.Bind( wx.EVT_BUTTON, self.number_input_seven )
		self.eigth.Bind( wx.EVT_BUTTON, self.number_input_eight )
		self.nine.Bind( wx.EVT_BUTTON, self.number_input_nine )
		self.multiply.Bind( wx.EVT_BUTTON, self.multi )
		self.four.Bind( wx.EVT_BUTTON, self.number_input_four )
		self.five.Bind( wx.EVT_BUTTON, self.number_input_five )
		self.six.Bind( wx.EVT_BUTTON, self.number_input_six )
		self.one.Bind( wx.EVT_BUTTON, self.number_input_one )
		self.two.Bind( wx.EVT_BUTTON, self.number_input_two )
		self.three.Bind( wx.EVT_BUTTON, self.number_input_three )
		self.zero.Bind( wx.EVT_BUTTON, self.number_input_zero )
		self.equal.Bind( wx.EVT_BUTTON, self.evaluate )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def radbuttom( self, event ):
		event.Skip()
	
	def inv( self, event ):
		event.Skip()
	
	def clear( self, event ):
		event.Skip()
	
	def number_input_seven( self, event ):
		event.Skip()
	
	def number_input_eight( self, event ):
		event.Skip()
	
	def number_input_nine( self, event ):
		event.Skip()
	
	def multi( self, event ):
		event.Skip()
	
	def number_input_four( self, event ):
		event.Skip()
	
	def number_input_five( self, event ):
		event.Skip()
	
	def number_input_six( self, event ):
		event.Skip()
	
	def number_input_one( self, event ):
		event.Skip()
	
	def number_input_two( self, event ):
		event.Skip()
	
	def number_input_three( self, event ):
		event.Skip()
	
	def number_input_zero( self, event ):
		event.Skip()
	
	def evaluate( self, event ):
		event.Skip()
	

