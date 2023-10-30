#!/usr/bin/python
#-*- coding: latin-1 -*-
import wx

fileA = open("toWrite.txt","w")
class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Fill the form", pos=(20, 30))
 
 
        self.button =wx.Button(self, label="Send", pos=(200, 200))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
 
        self.lblname  = wx.StaticText(self, label="Name: ", pos=(20,60))
        self.editname = wx.TextCtrl(self, value="", pos=(150, 60), size=(250,-1))

        self.lblmail  = wx.StaticText(self, label="email: ", pos=(20,90))
        self.editmail = wx.TextCtrl(self, value="", pos=(150, 90), size=(250,-1))
 
        self.lblinsti = wx.StaticText(self, label="Institution:", pos=(20,120))
        self.editinsti = wx.TextCtrl(self, value="", pos=(150, 120), size=(250,-1))
#	    self.lbllevel  = wx.StaticText(self, label="Tu grado o carrera :", pos=(20,150))
        self.editlevel = wx.TextCtrl(self, value="", pos=(150, 150), size=(250,-1))


        self.quote = wx.StaticText(self, label="Check your email", pos=(20, 180))
    def OnClick(self,event):
        self.logger.AppendText("Click on the object %dn" % event.GetId())



app = wx.App(False)
# Create the father frame
frame = wx.Frame(None, title="Welcome Earlham College", size=(540,350))
# Create a note block
nb = wx.Notebook(frame)
# add the panels with Addpage
nb.AddPage(ExamplePanel(nb), "Data")

frame.Show()
app.MainLoop()