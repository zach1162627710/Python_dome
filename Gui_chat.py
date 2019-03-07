import wx
import time
class myFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"weChat",size=(520,450))
        panel = wx.Panel(self)
        label_All = wx.StaticText(panel, -1, "All file",pos=(180, 0))
        self.text_All = wx.TextCtrl(panel,
                                    -1,
                                    size=(480,200),
                                    pos=(10,25),
                                    style=wx.TE_MULTILINE | wx.TE_READONLY)
        lable_I = wx.StaticText(panel, -1, "I say",pos=(180,220))
        self.text_I = wx.TextCtrl(panel,
                                  -1,
                                  size=(480,100),
                                  pos=(10,255),
                                  style=wx.TE_MULTILINE )

        self.buttonsend = wx.Button(panel,
                                    -1,
                                    "send",
                                    size=(75,25),
                                    pos=(180,360))
        self.buttonclear = wx.Button(panel,
                                     -1,
                                     "clear",
                                     size=(75,25),
                                     pos=(300,360))

        self.Bind(wx.EVT_BUTTON, self.OnButtonSend, self.buttonsend)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClear, self.buttonclear)

        btnsizer = wx.BoxSizer() #set a sub object
        btnsizer.Add(self.buttonsend, proportion=0) #add buttonsend on btnsizer
        btnsizer.Add(self.buttonclear, proportion=0)

        mainsizer = wx.BoxSizer(wx.VERTICAL) #creat a mainsizer(sub obj)
        mainsizer.Add(label_All, proportion=0, flag=wx.ALIGN_CENTER)
        mainsizer.Add(self.text_All, proportion=1, flag=wx.EXPAND)
        mainsizer.Add(lable_I, proportion=0, flag=wx.ALIGN_CENTER)
        mainsizer.Add(self.text_I, proportion=1, flag=wx.EXPAND)
        mainsizer.Add(btnsizer, proportion=0, flag=wx.ALIGN_CENTER)

        panel.SetSizer(mainsizer)

    def OnButtonSend(self, event):
        userinput = self.text_I.GetValue()
        self.text_I.Clear()
        now=time.ctime()
        inmsg="You (%s):\n%s  \n"%(now, userinput)
        self.text_All.AppendText(inmsg)  #text_I追加到 userinput
        #self.text_All.SetValue(userinput)　　


    def OnButtonClear(self,event):
        self.text_All.Clear()


if __name__ == "__main__":
    app = wx.App()
    frame = myFrame()
    frame.Show()
    app.MainLoop()

