# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 14:21:20 2018

@author: jon_c
"""
#
#from kivy.app import App
#from kivy.uix.widget import Widget
#from kivy.graphics import Color, Ellipse, Line
#
#
#class MyPaintWidget(Widget):
#
#    def on_touch_down(self, touch):
#        with self.canvas:
#            Color(1, 1, 0)
#            d = 30.
#            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
#            touch.ud['line'] = Line(points=(touch.x, touch.y))
#
#    def on_touch_move(self, touch):
#        touch.ud['line'].points += [touch.x, touch.y]
#
#
#class MyPaintApp(App):
#
#    def build(self):
#        return MyPaintWidget()
#
#
#if __name__ == '__main__':
#    MyPaintApp().run()
    
##%%
##video 1, 2 and 3
#from kivy.app import App
##from kivy.uix.button import Button
#from kivy.uix.scatter import Scatter
#from kivy.uix.label import Label
#from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.textinput import TextInput
#from kivy.uix.boxlayout import BoxLayout
#
#class ScatterTextWidget(BoxLayout):
#    pass
#
#
#class TutorialApp(App):
#    def build(self):
#        b = BoxLayout(orientation = "vertical")
#        t = TextInput(font_size = 150, size_hint_y = None, 
#                      height = 200, text = "default")
#        f = FloatLayout()
#        s = Scatter()
#        l = Label(text = "default", font_size = 150)
##        return Button(text = "Hello",
##                      background_color = (0,0,1,1), 
##                      font_size = 150)
#        
##        t.bind(text = some_function)
#        t.bind(text = l.setter("text"))
#        
#        f.add_widget(s)
#        s.add_widget(l)
#        
#        
#        b.add_widget(t)
#        b.add_widget(f)
#        return b
#
##def some_function(argument):
##    print ("text changed")
#
#
#if __name__ == "__main__":
#    TutorialApp().run()
    
    
#%%
#video 4
#from kivy.app import App
#from kivy.uix.scatter import Scatter
#from kivy.uix.label import Label
#from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.textinput import TextInput
#from kivy.uix.boxlayout import BoxLayout
#
#class ScatterTextWidget(BoxLayout):
#    pass
#    
#class TutorialApp(App):
#    def build(self):
#        return ScatterTextWidget()
#
#    
#if __name__ == "__main__":
#    TutorialApp().run()
#    
#%%
#video 5
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import random

class ScatterTextWidget(BoxLayout):
    def change_label_color(self, *args):
        color = [random.random() for i in range(3)] + [1]
        label = self.ids ["my_label"]
        label.color = color
    
class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()

    
if __name__ == "__main__":
    TutorialApp().run()
    
    
    
    
    
    
    
    
    
    