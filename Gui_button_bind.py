import wx
import turtle

class MyApp(wx.App):
    def OnInit(self):  #初始化
        frame = wx.Frame(parent=None,  #生成框架窗口
                         title='it\'s a App',
                         size=(400,300),
                         pos=(800,400))
        panel = wx.Panel(frame,-1)  #面板:白色
        self.buttonWJX = wx.Button(panel,
                                -1,
                                "五角星",
                                pos=(0,0))
        self.Bind(wx.EVT_BUTTON,self.OnButtonWJX,self.buttonWJX)

        self.buttonSJX = wx.Button(panel,
                                   -1,
                                   "三角形",
                                   pos=(100,0))
        self.Bind(wx.EVT_BUTTON,self.OnButtonSJX,self.buttonSJX)

        frame.Show()  #显示框架窗口
        return True

    def OnButtonWJX(self,event): #须绑定到 按钮上，这个函数须加一个 event的参数
        for i in range(5):
            turtle.forward(150)
            turtle.right(144)

    def OnButtonSJX(self,event):
        for i in range(3):
            turtle.forward(150)
            turtle.right(120)

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

