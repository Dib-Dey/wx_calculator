import scientific_panel
from scientific_panel import SciPanel
import wx

if __name__ == '__main__':
    app=wx.App()
    frame =wx.Frame(None, title = "Calculator_Panel_test",size = (600,500))
    panel_test = SciPanel(frame)
    frame.Show(True)
    app.MainLoop()