from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string('''
<cs3>
    cols:2
    font_size:32
    
    
    Label:
        text:'Investment Amount'
    TextInput:
        id:amount
        text:''
        multiline:False
    
        
    Label:
        text:'Years'
    TextInput:
        id:year
        text:''
        multiline:False
    
    Label:
        text:'Annual Interest Rate'
    TextInput:
        id:interest_rate
        text:''
        multiline:False
   
    Label:
        text:'Future Value'
    Label:
        id:future
        text:''
        multiline:False
    
    
    Button:
        text:'Calculate'
        on_press:root.calculate()
    Label:
        text:''    
        

''')

class cs3(BoxLayout):
    def calculate(self):
        output = round(float(self.ids.amount.text)*(1+float(self.ids.interest_rate.text)/12*0.01)**(float(self.ids.year.text)*12),2)
        self.ids.future.text=str(output)
        

class cs3App(App):
    def build(self):
        return cs3()

cs3App().run()
