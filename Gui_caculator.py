# -*- coding: cp936 -*-
import wx
from math import *

class my_caculator(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,
                          None,
                          -1,
                          "������",
                          size=(350,480),
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | #��^��:ȥ����ק�ı�Frame��С���ԣ�ȥ����󻯣�ȥ����С��
                                                          wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))
        panel = wx.Panel(self)
        boxsize = wx.BoxSizer(wx.VERTICAL)  #���ֹ�����
        gridbox= wx.GridSizer(rows=6, cols=5, hgap=5, vgap=5) #��ά���������  6��5��  ���5����
        self.equation = ""
        self.textprint=wx.TextCtrl(panel, -1, '',style=wx.TE_MULTILINE | wx.TE_READONLY)  # ����  ֻ��

        #��ť
        self.buttononData = "7 8 9 Del AC 4 5 6 * / 1 2 3 + - 0 % pi e sqrt ^ sin cos tan log ln ( ) . =".split()
        buttonLength = len(self.buttononData)
        for i in range(buttonLength):
            labels = '%s' % self.buttononData[i]
            buttonIterm = wx.Button(panel, i, labels, size=(63,63))
            gridbox.Add(buttonIterm, 0, 0)  #buttonIterm���뵽gridbox��ά������
            self.creatHandel(buttonIterm, labels)
        boxsize.Add(self.textprint, 1, wx.EXPAND)  #������
        boxsize.Add(gridbox, 5, wx.EXPAND)
        panel.SetSizerAndFit(boxsize)  #��boxsize����panel��

    #����������
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
        eventbutton = event.GetEventObject()   #GetEventObject������ȡ��event�¼���صĿؼ�
        labels = eventbutton.GetLabel()        #GetLabel()����ȡ��ť�ı�ǩ,��������֪������ ���� �ǳ���Del AC =�����ĸ���ť��
        self.equation += labels                #����Щ��ť�ı�ǩ�������ʾ�ķ��ţ�׷�ӵ� self.equation
        self.textprint.SetValue(self.equation) #��ӡ����

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
            target = eval(string)                 #eval() ����ʵ��list��dict��tuple��str֮���ת��

            self.equation += '=' + str(target)    #str()  ��list��dict��tupleתΪΪ�ַ���
            self.textprint.SetValue(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self,
                                   "��������ȷ���ʽ",
                                    "��ע��",
                                    wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

if __name__ == "__main__":
    app = wx.App()
    frame = my_caculator()
    frame.Show()
    app.MainLoop()
