#!/usr/bin/env python3.6
import wx
import classic_panel
import prog_panel
import os
current_dir = os.getcwd()
image_dir = os.path.join(current_dir,"Image")

class MainFrame(wx.Frame):
    """This is the mainframe of the calculator where all panels are defined"""
    def __init__(self):
        super().__init__(None, title = "Calculator",size = (600,600))
        self.classic_panel = classic_panel.ClassicPanel(self)
        self.sci_panel = prog_panel.ProgPanel(self)

        self.sci_panel.Hide()
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.classic_panel, 1, wx.EXPAND)
        self.sizer.Add(self.sci_panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.SetMenuBar(self.CreateMenuBar())
        self.CreatetoolBar()

    def CreatetoolBar(self):
        """Create toolbar"""
        self.toolbar_main = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
        self.toolbar_main.SetToolBitmapSize(wx.Size(1, 1))
        self.toolbar_main.SetToolSeparation(0)
        self.toolbar_main.SetFont(wx.Font(8, 74, 90, 90, False, "Arial"))
        self.toolbar_main.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVEBORDER))
        self.toolbar_main.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))
        self.toolbar_main.SetMaxSize(wx.Size(-1, 2))
        self.toolbar_main.AddSeparator()
        self.tool_classic= self.toolbar_main.AddTool(201, u"tool",
                                                      wx.Bitmap(os.path.join(u"./Image/classic.bmp"), wx.BITMAP_TYPE_ANY),
                                                      wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString,
                                                      None)

        self.toolbar_main.AddSeparator()
        self.tool_sci = self.toolbar_main.AddTool(202, u"tool",
                                                      wx.Bitmap(os.path.join(u"./Image/sci.bmp"), wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                      wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)
        self.toolbar_main.Realize()
        self.Centre(wx.BOTH)
        self.Bind(wx.EVT_TOOL, self.swtich, id=201)
        self.Bind(wx.EVT_TOOL, self.swtich, id=202)

    def CreateMenuBar(self, with_window=False):
        """Make a menubar"""
        menu_bar = wx.MenuBar()
        option_menu = wx.Menu()
        menu_bar.Append(option_menu, "&Options")
        option_item_exit = option_menu.Append(wx.ID_EXIT, 'Quit')
        self.Bind(wx.EVT_MENU, self.exit, id=wx.ID_EXIT)
        option_menu.Append(201, 'Classic Calculator')
        self.Bind(wx.EVT_MENU, self.swtich, id=201)
        option_menu.Append(202, 'Scientific Calculator')
        self.Bind(wx.EVT_MENU, self.swtich, id=202)
        help_menu = wx.Menu()
        help_menu_item = help_menu.Append(wx.ID_HELP, 'Help')
        menu_bar.Append(help_menu, "&Help")
        return menu_bar

    def exit(self, evt):
        self.Close()

    def swtich(self,evt):
        """helps switching between different panel from the menu"""
        if evt.GetId() == 201:
            if self.classic_panel.IsShown():
                pass
            else:
                self.SetTitle("Classic Calculator")
                self.sci_panel.Hide()
                self.classic_panel.Show()
        else:
            if self.sci_panel.IsShown():
                pass
            else:
                self.SetTitle("Scientific Calculator")
                self.classic_panel.Hide()
                self.sci_panel.Show()
        self.Layout()

if __name__ == '__main__':
    """Run the main Gui from here"""
    app = wx.App()
    MainFrame = MainFrame()
    MainFrame.Show(True)
    app.MainLoop()