# -*- coding: cp936 -*-
import wx
from math import *


class Calculator(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "������", size=(350, 480),
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER |
                                                          wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))
        panel = wx.Panel(self)
        boxsize = wx.BoxSizer(wx.VERTICAL)
        gridBox = wx.GridSizer(rows=6, cols=5, hgap=5, vgap=5)
        self.equation = ""  # ��¼��ʽ

        #self.statictext = wx.StaticText(panel,-1,'')
        self.textprint = wx.TextCtrl(panel, -1, '', style=wx.TE_MULTILINE | wx.TE_READONLY)

        # ��ť����
        self.buttonData = "7 8 9 DEL AC 4 5 6 * / 1 2 3 + - 0 % pi e sqrt ^ sin cos tan log ln ( ) . =".split()
        buttonLength = len(self.buttonData)
        for i in range(buttonLength):
            labels = "%s" % self.buttonData[i]
            buttonIterm = wx.Button(panel, i, labels, size=(63, 52))
            self.createHandler(buttonIterm, labels)
            gridBox.Add(buttonIterm, 0, 0)
        boxsize.Add(self.textprint, 1, wx.EXPAND)
        boxsize.Add(gridBox, 5, wx.EXPAND)
        panel.SetSizerAndFit(boxsize)

    # ����������
    def createHandler(self, button, labels):
        item = "DEL AC ="
        if labels not in item:
            self.Bind(wx.EVT_BUTTON, self.OnAppend, button)
        elif labels == 'DEL':
            self.Bind(wx.EVT_BUTTON, self.OnDel, button)
        elif labels == 'AC':
            self.Bind(wx.EVT_BUTTON, self.OnAc, button)
        elif labels == '=':
            self.Bind(wx.EVT_BUTTON, self.OnTarget, button)

    # ��������������
    def OnAppend(self, event):
        eventbutton = event.GetEventObject()
        label = eventbutton.GetLabel()
        self.equation += label
        self.textprint.SetValue(self.equation)

    def OnDel(self, event):
        self.equation = self.equation[:-1]
        self.textprint.SetValue(self.equation)

    def OnAc(self, event):
        self.textprint.Clear()
        self.equation = ""


    def OnTarget(self, event):
        string = self.equation
        if '^' in string:
            string = string.replace('^', '**')
        try:
            target = eval(string)
            self.equation += '=' + str(target)
            self.textprint.SetValue(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self, '��������ȷ�ĵ�ʽ!', '��ע��',
                                   wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = Calculator()
    frame.Show()
    app.MainLoop()
