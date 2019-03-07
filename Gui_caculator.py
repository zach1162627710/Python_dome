# -*- coding: cp936 -*-
import wx
from math import *

class my_caculator(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,
                          None,
                          -1,
                          "计算器",
                          size=(350,480),
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | #“^”:去除拖拽改变Frame大小属性，去除最大化，去除最小化
                                                          wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))
        panel = wx.Panel(self)
        boxsize = wx.BoxSizer(wx.VERTICAL)  #布局管理器
        gridbox= wx.GridSizer(rows=6, cols=5, hgap=5, vgap=5) #二维网格管理器  6行5列  间隔5像素
        self.equation = ""
        self.textprint=wx.TextCtrl(panel, -1, '',style=wx.TE_MULTILINE | wx.TE_READONLY)  # 多行  只读

        #按钮
        self.buttononData = "7 8 9 Del AC 4 5 6 * / 1 2 3 + - 0 % pi e sqrt ^ sin cos tan log ln ( ) . =".split()
        buttonLength = len(self.buttononData)
        for i in range(buttonLength):
            labels = '%s' % self.buttononData[i]
            buttonIterm = wx.Button(panel, i, labels, size=(63,63))
            gridbox.Add(buttonIterm, 0, 0)  #buttonIterm加入到gridbox二维网格中
            self.creatHandel(buttonIterm, labels)
        boxsize.Add(self.textprint, 1, wx.EXPAND)  #最大化填充
        boxsize.Add(gridbox, 5, wx.EXPAND)
        panel.SetSizerAndFit(boxsize)  #将boxsize放入panel中

    #创建处理方法
    def creatHandel(self, button, labels):
        item = "Del AC ="
        if labels not in item:
            self.Bind(wx.EVT_BUTTON, self.OnAppend, button)
        elif labels == "Del":
            self.Bind(wx.EVT_BUTTON, self.onDel, button)
        elif labels == "AC":
            self.Bind(wx.EVT_BUTTON, self.onAC, button)
        elif labels == "=":
            self.Bind(wx.EVT_BUTTON, self.onTarget, button)

    def OnAppend(self, event):
        eventbutton = event.GetEventObject()   #GetEventObject方法获取和event事件相关的控件
        labels = eventbutton.GetLabel()        #GetLabel()来获取按钮的标签,这样就能知道你所 按得 是除“Del AC =”外哪个按钮了
        self.equation += labels                #将这些按钮的标签（上面标示的符号）追加到 self.equation
        self.textprint.SetValue(self.equation) #打印出来

    def onDel(self,event):
        self.equation = self.equation[:-1]
        self.textprint.SetValue(self.equation)

    def onAC(self, event):
        self.textprint.Clear()
        self.equation = ''

    def onTarget(self, event):
        string = self.equation
        if '^' in string:
            string = string.replace('^','**')
        try:
            target = eval(string)                 #eval() 就是实现list、dict、tuple与str之间的转化

            self.equation += '=' + str(target)    #str()  把list，dict，tuple转为为字符串
            self.textprint.SetValue(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,
                                   "请输入正确表达式",
                                    "请注意",
                                    wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

if __name__ == "__main__":
    app = wx.App()
    frame = my_caculator()
    frame.Show()
    app.MainLoop()
