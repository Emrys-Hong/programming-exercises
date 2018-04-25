from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.uix.togglebutton import ToggleButton
from firebase import firebase
from kivy.lang import Builder

token = "xbFBK0N1I9Id5ljHZAS9QitRXNdZzb0S3ZsAi1vH"
url = "https://checkoff-6e917.firebaseio.com/"
firebase = firebase.FirebaseApplication(url,token)

Builder.load_string("""
<GuiKivy>
    rows: 2

    BoxLayout:
        cols: 2
        Label:
            text: "Yellow LED"
        ToggleButton:
            id: yellow
            text: "OFF"
            multiline: False
            state: 'normal'
            on_press: root.updateYellow()
            
    BoxLayout:
        cols:2
        Label:
            text: "Red LED"
        ToggleButton:
            id: red
            text: "OFF"
            state: 'normal'
            on_press: root.updateRed()
            
""")
class GuiKivy(GridLayout):
    def __init__(self):
        super().__init__()
        
        self.ids.yellow.state = firebase.get('/yellow_state')
        self.ids.red.state = firebase.get('/red_state')
    
    def updateYellow(self):
        if self.ids.yellow.text == 'OFF':
            self.ids.yellow.text = "ON"
            self.ids.yellow.state = "down"
            self.ids.yellow.background_color = (0, 0, 1, 0.7)
            firebase.put("/","yellow_state","down")
        else:
            self.ids.yellow.text = "OFF"
            self.ids.yellow.state = "normal"
            self.ids.yellow.background_color = (1, 1, 1, 1)
            firebase.put("/","yellow_state","normal")


    d = 1
    def updateRed(self):
        if self.ids.red.text == 'OFF':
            self.ids.red.text = "ON"
            self.ids.red.state = "down"
            self.ids.red.background_color = (0, 0, 1, 0.7)
            firebase.put("/","red_state","down")
        else:
            self.ids.red.text = "OFF"
            self.ids.red.state = "normal"
            self.ids.red.background_color = (1, 1, 1, 1)
            firebase.put("/","red_state","normal")

class GuiKivyApp(App):
    def build(self):
        return GuiKivy()  
    
# =============================================================================
#     def update_status(self, instance):
#     # use this callback to update firebase
#         
# =============================================================================
    
GuiKivyApp().run()