import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string('''
<Slide>
    Label:
        id: slidetxt
        text: 'Slide Me'
        font_size : 72
        on_touch_move: root.on_touch_move()
        
''')

class Slide(BoxLayout):
    def on_touch_move(self, touch):
        if touch.dx > 40:
            self.ids.slidetxt.text = 'Slide Right'
        if touch.dx < -40:
            self.ids.slidetxt.text = 'Slide Left'
        if touch.dy > 25:
            self.ids.slidetxt.text = 'Slide Up'
        if touch.dy < -25:
            self.ids.slidetxt.text = 'Slide Down'

class SlideApp(App):
    def build(self):
        return Slide()
SlideApp().run()
