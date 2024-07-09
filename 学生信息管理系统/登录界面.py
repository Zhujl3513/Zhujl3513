import os
from turtle import title
import pysql
import wx

#import userd

niu = ["登录", "注册", "管理员登陆", "退出"]



class TestFrm(wx.Frame):
    """TestFrm"""

    def __init__(self, parent, title):
        super(TestFrm, self).__init__(parent, title=title,
                                      size=(800, 600))  # 定义标题大小
        self.panel = wx.Panel(self, -1)
        self.parent = parent
        self.title = title
        self.box = wx.BoxSizer(wx.HORIZONTAL)
        wx.StaticText.SetBackgroundColour(self, (102, 204, 255))  ##背景颜色
        for i in niu:  ##循环定义菜单按钮
            btn = wx.Button(self.panel, 1, label="{}".format(i))
            btn.Bind(wx.EVT_BUTTON, lambda e, mark=i: self.on_click(e, mark))
            self.box.Add(btn, 1, wx.LEFT)
        self.panel.SetSizer(self.box)
        self.Centre()
        self.Show()

    def on_click(self, event, mark):
        self.mark = mark
        if self.mark == '退出':
            wx.Exit()
        if self.mark == '注册':
            self.srcinput(self.mark)
        if self.mark == '登录':
            self.srcinput(self.mark)

        if self.mark == '管理员登陆':
            self.srcinput(self.mark)

    def on_click1(self, event, mark):
        self.panel = wx.Panel(self, -1)
        self.box = wx.BoxSizer(wx.HORIZONTAL)

    def srcinput(self, i):
        panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(10, 10)
        self.box.ShowItems(False)
        text = wx.StaticText(self.panel, label="用户名 :")
        self.sizer.Add(text, pos=(4, 5), flag=wx.TOP | wx.BOTTOM, border=13)
        text = wx.StaticText(self.panel, label="密 码 :")
        self.sizer.Add(text, pos=(5, 5), flag=wx.TOP | wx.BOTTOM, border=13)

        self.tc1 = wx.TextCtrl(self.panel, -1)  ##输入框
        self.sizer.Add(self.tc1, pos=(4, 6), span=(1, 8), flag=wx.TOP | wx.EXPAND)
        self.tc2 = wx.TextCtrl(self.panel, -1, style=wx.TE_PASSWORD)
        self.sizer.Add(self.tc2, pos=(5, 6), span=(1, 8), flag=wx.TOP | wx.EXPAND)
        if self.mark == '注册':
            text = wx.StaticText(self.panel, label="重复密码:")
            self.sizer.Add(text, pos=(6, 5), flag=wx.TOP | wx.BOTTOM, border=13)
            self.tc3 = wx.TextCtrl(self.panel, -1, style=wx.TE_PASSWORD)
            self.sizer.Add(self.tc3, pos=(6, 6), span=(1, 8), flag=wx.TOP | wx.EXPAND, border=5)

        self.button = wx.Button(self.panel, label="{}".format(i), size=(90, 28))
        self.sizer.Add(self.button, pos=(8, 7), flag=wx.RIGHT | wx.BOTTOM, border=5)
        self.Bind(wx.EVT_BUTTON, self.on_button, self.button)
        self.button1 = wx.Button(self.panel, label="返回", size=(90, 28))
        self.sizer.Add(self.button1, pos=(8, 9), flag=wx.RIGHT | wx.BOTTOM, border=5)
        self.Bind(wx.EVT_BUTTON, self.rut, self.button1)
        self.panel.SetSizerAndFit(self.sizer)

    def rut(self, event):
        wx.Exit()
        self.app = wx.App()
        self.frm = TestFrm(None, title="xitong")
        self.frm.Show()
        self.app.MainLoop()

    def on_button(self, event):
        uname = self.tc1.GetValue()
        upass = self.tc2.GetValue()
        if self.mark == '登录':
            a = pysql.dl(uname, upass)
            if a == 1:
                wx.MessageDialog(self, '{}成功'.format(
                    self.mark), '{}中'.format(self.mark), wx.ICON_INFORMATION).ShowModal()
                pysql.addhc(uname)
                os.system('userd.py')
            if a == 0:
                wx.MessageDialog(self, '{}失败，密码不正确'.format(
                    self.mark), '{}中'.format(self.mark), wx.ICON_INFORMATION).ShowModal()
            if a == 2:
                wx.MessageDialog(self, '{}失败，用户名不正确'.format(
                    self.mark), '{}中'.format(self.mark), wx.ICON_INFORMATION).ShowModal()
        if self.mark == '注册':
            usern = self.tc3.GetValue()
            a = pysql.logon(uname, upass, usern)
            if a == 1:
                wx.MessageDialog(self, '{}成功'.format(
                    self.mark), '{}中'.format(self.mark), wx.ICON_INFORMATION).ShowModal()
            if a == 2:
                wx.MessageDialog(self, '请重新输入密码', '确认', wx.ICON_INFORMATION).ShowModal()
            if a == 3:
                wx.MessageDialog(self, '用户名已存在,请重新注册！！', '确认', wx.ICON_INFORMATION).ShowModal()
            if a == 4:
                wx.MessageDialog(self, '您两次输入密码不相同，请重新输入！', '确认', wx.ICON_INFORMATION).ShowModal()
        if self.mark == '管理员登陆':
            a = pysql.dl(uname, upass)
            if a == 1:
                wx.MessageDialog(self, '{}成功'.format(
                    self.mark), '{}'.format(self.mark), wx.ICON_INFORMATION).ShowModal()
            wx.Exit()
            os.system('guanli.py')


if __name__ == '__main__':
    app = wx.App()
    frm = TestFrm(None, title="xitong")
    frm.Show()
    app.MainLoop()

