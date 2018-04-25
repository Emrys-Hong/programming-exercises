from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
<cs4>
    transition:FadeTransition()
    Screen:
        name:'scn1'
        BoxLayout:
            Button:
                id:scn1_btn1
                text:'Settings'
                font_size:32
                on_release:root.current='scn2' #once release--screen2
            Button:
                id:scn1)btn2
                text:'Quit'
                font_size:32
                on_press:root.on_stop()
    Screen:
        name:'scn2'
        BoxLayout:
            cols:2
            Label:
                text:'Settings'
                font_size:32
                color:1,0,0,1
            Button:
                id:scn2_btn1
                text:'Back'
                font_size:32
                on_release:root.current='scn1'

''')
class cs4(ScreenManager):
    def on_stop(self):
        App.get_running_app().stop()

class cs4App(App):
    def build(self):
        return cs4()

cs4App().run()
        
        
