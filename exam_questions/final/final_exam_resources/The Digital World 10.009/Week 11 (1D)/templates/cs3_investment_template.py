from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 

class MyLabel(Label):
	def __init__(self,**kwargs):
		Label.__init__(self,**kwargs)
		self.bind(size=self.setter('text_size'))
		self.padding=(20,20)

class Investment(App):

	def build(self):
		layout= GridLayout(cols=2)
		l1=MyLabel(text="Investment Ammount",font_size=24,halign='left',valign='middle')
		layout.add_widget(l1)
		pass 
		btn = Button(text="Calculate", on_press=self.calculate, font_size=24)
		layout.add_widget(btn)
		return layout 

	def calculate(self, instance):
		inv_amt = None
		years = None
		mth_int_rate = None
		self.txt_future_val.text=None



Investment().run()