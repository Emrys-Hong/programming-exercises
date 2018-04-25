import kivy
# kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder

# ### Buttons
# Builder.load_string('''
# <second>
#     BoxLayout:
#         orientation:'veritcal'
#         Button:
#             text:'Begin'
#             font_size:32
#         Button:
#             text: 'Quit'
#             font_size: 32
#             on_press: root.on_stop()
# ''')
# class MyApp(App):
#     def build(self):
#         layout = BoxLayout(orientation = 'vertical')
#         self.btn1 = Button(text = 'Begin')
#         self.btn2 = Button(text = 'Quit')
#         layout.add_widget(self.btn1)
#         layout.add_widget(self.btn2)
#         return layout
# class secondapp(BoxLayout):
#     def on_stop(selfself):
#         App.get_running_app().stop()
# class secondapp(App):
#     def build(self):
#         return secondapp
# if __name__ == '__main__':
#     MyApp().run()



## alternate
Builder.load_string('''
<cs1>
    Label:
        id:label1
        text: 'Is Programming Fun?'
        font_size: 32

        on_touch_down: root.updateAlt()
        ''')

class cs1(BoxLayout):
    c = 1
    def updateAlt(self):
        self.c += 1
        if self.c%2 == 0:
            self.ids.label1.text = 'Yes It is fun!'
        else:
            self.ids.label1.text = 'Is Programming Fun?'
class cs1App(App):
    def build(self):
        return cs1()
cs1App().run()


