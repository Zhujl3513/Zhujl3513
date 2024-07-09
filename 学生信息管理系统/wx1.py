import wx
from project import Student

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='WxPython Demo', size=(350, 250))
        panel = wx.Panel(self)

        self.text_ctrl = wx.TextCtrl(panel, pos=(20, 20))
        self.button = wx.Button(panel, label='Click Me', pos=(20, 60))
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)

    def on_button_click(self, event):
        message = self.text_ctrl.GetValue()
        wx.MessageBox(message, 'Message', wx.OK | wx.ICON_INFORMATION)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
    s = Student()
    s.run()