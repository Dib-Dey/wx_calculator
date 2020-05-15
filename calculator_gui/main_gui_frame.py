import wx
import classic_panel
import scientific_panel

class MainFrame(wx.Frame):
    """This is the mainframe of the calculator where all panels are defined"""
    def __init__(self):
        super().__init__(None, title = "Calculator",size = (600,500))
        self.classic_panel = classic_panel.ClassicPanel(self)
        self.sci_panel = scientific_panel.SciPanel(self)
        self.sci_panel.Hide()
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.classic_panel, 1, wx.EXPAND)
        self.sizer.Add(self.sci_panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.SetMenuBar(self.CreateMenuBar())

    def CreateMenuBar(self, with_window=False):
        # Make a menubar
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
    app = wx.App()
    MainFrame = MainFrame()
    MainFrame.Show(True)
    app.MainLoop()