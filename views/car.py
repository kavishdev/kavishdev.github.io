﻿#!/bin/python3
import gi
import os,sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class HeaderBarWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Car Control")
        self.set_border_width(10)
        self.set_default_size(400, 300)
        
        #self.set_icon_from_file("icon.svg")
        
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Car Control"
        self.set_titlebar(hb)
        
        
        btRight=Gtk.Button(label="Right")
        btRight.connect('clicked',self.right)
        btRight.set_halign(Gtk.Align.END)
        btRight.set_valign(Gtk.Align.CENTER)    
        
        
        
        btLeft=Gtk.Button(label="Left")
        btLeft.connect('clicked', self.left)
        btLeft.set_halign(Gtk.Align.START)
        btLeft.set_valign(Gtk.Align.CENTER)    

        btForward=Gtk.Button(label="Forward")
        btForward.connect('clicked',self.forward)
        btForward.set_halign(Gtk.Align.CENTER)
        btForward.set_valign(Gtk.Align.START)    



        btBackward=Gtk.Button(label="Backward")
        btBackward.connect('clicked',self.backward)
        btBackward.set_halign(Gtk.Align.CENTER)
        btBackward.set_valign(Gtk.Align.END)    



        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        button = Gtk.Button()
        button.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.LEFT, shadow_type=Gtk.ShadowType.NONE)
        )
        box.add(button)

        button = Gtk.Button()
        button.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.RIGHT, shadow_type=Gtk.ShadowType.NONE)
        )
        box.add(button)

        #hb.pack_start(box)
        
        mainbox=Gtk.Box()
        self.add(mainbox)


        btRight.set_property("width-request", 100)
        btRight.set_property("height-request", 30)
        
        btBackward.set_property("width-request", 100)
        btBackward.set_property("height-request", 30)
        
        btLeft.set_property("width-request", 100)
        btLeft.set_property("height-request", 30)
        
        btForward.set_property("width-request", 100)
        btForward.set_property("height-request", 30)
            

        mainbox.pack_start(btLeft,True,True, 0)
        
        
        mainbox.pack_start(btBackward,True,True,0)

        mainbox.pack_start(btForward,True,True,0)

        mainbox.pack_start(btRight,True,True,0)
        
        
        
        #grid = Gtk.Grid()
        
        
        #grid.add(btRight)
        #grid.attach(btForward, 1, 0, 2, 1)
        #grid.attach_next_to(btLeft, btRight, Gtk.PositionType.BOTTOM, 1, 2)
        #grid.attach_next_to(btForward,btBackward, Gtk.PositionType.RIGHT, 2, 1)

        #self.add(grid)  

    def right(self, button) :
        os.system("curl 192.168.1.73/left")
       
    def left(self, button):
        os.system("curl 192.168.1.73/right")
       
    def forward(self, button):
        os.system("curl 192.168.1.73/forward")
       
    def backward(self, button):
        os.system("curl 192.168.1.73/backward") 




win = HeaderBarWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
