# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 11:07:57 2018

@author: jon_c
"""

#from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.button import Button
#
#
#class firstapp(App):
#    
#    def build(self):
#        layout = BoxLayout(orientation = "vertical")
#        self.btn1 = Button(text = "Begin")
#        self.btn2 = Button(text = "Quit")
#        self.btn2.bind(on_press = self.on_stop)
#        layout.add_widget(self.btn1)
#        layout.add_widget(self.btn2)
#        return layout
#    
#firstapp().run()



#%%
#from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.button import Button
#from kivy.lang import Builder
#
#Builder.load_string("""
#<secondapp>
#    BoxLayout:
#        orientation: "vertical"
#        Button:
#            text: "Begin"
#            font_size: 32
#        Button: 
#            text: "Quit"
#            font_size: 32
#            on_press: root.on_stop()
#         
#        """)
#
#class secondapp(BoxLayout):
#    def on_stop(self):
#        App.get_running_app().stop()
#
#class secondappApp(App):
#    def build(self):
#        return secondapp()
#    
#    
#secondappApp().run()
#%%
#from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.button import Button
#from kivy.lang import Builder
#
#
#Builder.load_string("""
#<lunch>
#    orientation: "vertical"
#    Label:
#        text: "What's for lunch?"
#        font_size: 32
#    BoxLayout: 
#        orientation: "horizontal"
#        Button:
#            text: "Chicken Rice"
#            font_size: 32
#            on_press: root.menu("Chicken Rice")
#        Button:
#            text: "Health Soup"
#            font_size: 32
#            on_press: root.menu("Health Soup")
#            
#    Label:
#        id: result
#        font_size: 32
#        text: " "
#        
#    Label:
#        id: output
#        font_size: 32
#        text: " "
#        
#""")
#
#class lunch(BoxLayout):
#    def __init__(self):
#        super().__init__()
#        self.chicken = 0
#        self.soup = 0
#        
#    def menu(self, guess):
#        output = "You ordered " + guess
#        self.ids.result.text = output
#        if guess == "Chicken Rice":
#            self.chicken += 1
#        elif guess == "Health Soup":
#            self.soup += 1
#            
#
#class lunchApp(App):
#    def build(self): 
#        return lunch
#    
#lunchApp().run()

#%%
#question 1
#from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout
#from kivy.lang import Builder
#
#Builder.load_string("""
#<cs1>
#    Label:
#        id: label1
#        text: "Is programming fun?"
#        font_size: 32
#        on_touch_down:root.updateAlt()
#            """)
#
#class cs1(BoxLayout):
#    c = 1
#    def updateAlt(self):
#        self.c += 1
#        if self.c % 2 ==0:
#            self.ids.label1.text = "Yes it's fun!"
#        else:
#            self.ids.label1.text = "Is programming fun?"
#
#class cs1App(App):
#    def build(self):
#        return cs1()
#    
#cs1App().run()

#%%
#question 2
#from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.button import Button
#from kivy.lang import Builder
#
#Builder.load_string("""
#<Slide>
#    Label:
#        id: slidetxt
#        text: "Slide"
#        font_size: 72
#        on_touch_move:root.on_touch_move()
#""")
#
#
#class Slide(BoxLayout):
#    def on_touch_move(self,touch):
#        if touch.dx > 40:
#            self.ids.slidetxt.text = "Slide right"
#
#        elif touch.dx < -40:
#            self.ids.slidetxt.text = "Slide left"
#
#        elif touch.dy > 20:
#            self.ids.slidetxt.text = "Slide up"
#
#        elif touch.dy < -20:
#            self.ids.slidetxt.text = "Slide down"
#
#        
#class SlideApp(App):
#    def build(self):
#        return Slide()
#
#SlideApp().run()

#%%
#question 3
#from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.button import Button
#from kivy.uix.gridlayout import GridLayout
#from kivy.lang import Builder
#
#Builder.load_string("""
#<calculator>
#    rows: 5
#        
#    BoxLayout:
#        Label:
#            text: "Investment-value calculator"
#            font_size: 30
#
#    BoxLayout:
#        cols: 2
#        Label:
#            text: "Investment Amount"
#        TextInput:
#            id: amt
#            text: ""
#            multiline: False
#            
#    BoxLayout:
#        cols: 2
#        Label:
#            text: "Years"
#        TextInput:
#            id: duration
#            text: ""
#            multiline: False
#            
#    BoxLayout:
#        cols: 2
#        Label:
#            text: "Annual Interest Rate"
#        TextInput:
#            id: rate
#            text: ""
#            multiline: False
#            
#    BoxLayout:
#        cols: 2
#        Button:
#            text: "Calculate"
#            on_press: root.calculate()
#        Label:
#            id: out
#            text: ""
#                
#""")
#
#class calculator(GridLayout):
#    def calculate(self):
#        returns = float(self.ids.amt.text) * (1 + (float(self.ids.rate.text)) / 1200) ** ((float(self.ids.duration.text)) * 12)   
#        self.ids.out.text = str(round(returns, 2))
#
#class calculatorApp(App):
#    def build(self):
#        return calculator()   
#    
#calculatorApp().run()

#%%
#question 4
#from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.button import Button
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.screenmanager import ScreenManager
#from kivy.lang import Builder
#
#Builder.load_string("""
#<screenswitch>
#    Screen:
#        name: "screen1"
#        BoxLayout:
#            Button:
#                id: screen1_button1
#                text: "Settings"
#                font_size: 32
#                on_release:root.current="screen2"
#            Button:
#                id: screen1_button2
#                text: "QUIT"
#                font_size: 32
#                on_release:root.on_stop()
#    
#    Screen:
#        name: "screen2"
#        BoxLayout:
#            cols: 2
#            Label:
#                text: "Settings"
#                font_size: 32
#            Button:
#                id: screen2_button1
#                text: "Back"
#                font_size: 32
#                on_release:root.current="screen1"
#                
#""")
#
#class screenswitch(ScreenManager):
#    def on_stop(self):
#        App.get_running_app().stop()
#           
#class screenswitchApp(App):
#    def build(self):
#        return screenswitch()
#    
#screenswitchApp().run()

#%%







































