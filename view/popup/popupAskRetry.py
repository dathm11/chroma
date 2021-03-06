#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Serge Watchou
"""
from utils.require import require
require("tkinter")
from tkinter import Tk,Button,PanedWindow,Label,Frame
import time

__all__ =['Popup',]

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

class Popup:
    def __init__(self):
        self.displayPopup = True
    def getPopup(self):
        return self.popup
    def popupAskRetry(self,title="Warning",message="popupAskRetry"):
        if self.displayPopup:
            #popup
            self.popup = Tk()
            self.popup.wm_title(title)

            frame = Frame(self.popup)
            panedWindow = PanedWindow(frame)

            #icon warning
            labelIconWarning = Label(panedWindow,image="::tk::icons::warning")
            panedWindow.add(labelIconWarning)

            #text
            labelMessage = Label(panedWindow,text=message,font=NORM_FONT)
            panedWindow.add(labelMessage)

            #button
            buttonOk = Button(frame,text="Ré-essayer")

            #display
            panedWindow.pack(side="top")
            buttonOk.pack(side="bottom")
            frame.pack(side="top", fill="x", padx=10, expand = True)
        else:
            self.popup.focus_force()
        self.popup.mainloop()

    def popupInformation(self,title="Info",message="Info"):
        if self.displayPopup:
            #popup
            self.popup = Tk()
            self.popup.wm_title(title)

            frame = Frame(self.popup)
            panedWindow = PanedWindow(frame)

            #icon warning
            labelIconWarning = Label(panedWindow,image="::tk::icons::information")
            panedWindow.add(labelIconWarning)

            #text
            labelMessage = Label(panedWindow,text=message,font=NORM_FONT)
            panedWindow.add(labelMessage)

            #button
            buttonOk = Button(frame,text="Ok")

            #display
            panedWindow.pack(side="top")
            buttonOk.pack(side="bottom")
            frame.pack(side="top", fill="x", padx=10, expand = True)
        else:
            self.popup.focus_force()
        self.popup.mainloop()   



    def quit(self,event=None):
        self.popup.quit()
        self.displayPopup=False 
    def destroy(self):
        if not self.displayPopup:
            self.popup.destroy()