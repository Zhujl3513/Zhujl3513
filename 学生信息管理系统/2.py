import wx
import mysql.connector

class MyFrame(wx.Frame):
    def __init__(self, title):
        super(MyFrame, self).__init__(None, title=title, size=(400, 300))

        self.InitUI()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        # 创建一个文本框来显示查询结果
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)

        # 创建一个按钮来触发数据库查询
        btn = wx.Button(panel, label='Query Database')
        btn.Bind(wx.EVT_BUTTON, self.OnQuery)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.text_ctrl, 1, wx.EXPAND | wx.ALL, 10)
        sizer.Add(btn, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        panel.SetSizer(sizer)

    def OnQuery(self, e):
        # 连接到MySQL数据库


        cnx = mysql.connector.connect(
            host="127.0.0.1",  # MySQL服务器地址
            user="root",  # 用户名
            password="1234567890",  # 密码
            database="sys"  # 数据库名称
        )



        cursor = cnx.cursor()

        # 执行查询
        query = "use sys;SELECT * FROM 爬取东方财富14年数据"
        cursor.execute(query)

        # 获取查询结果并显示
        #for (id, name, ...) in cursor:
            #self.text_ctrl.AppendText(f"ID: {id}, Name: {name}, ...\n")

        results = cursor.fetchall()

        for row in results:
            print(row)


        # 关闭连接
        cursor.close()
        cnx.close()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame('wxPython & MySQL Example')
    app.MainLoop()