from kivy.app import App
from kivy.uix.label import Label 

class SlideDetectApp(App):
	def build(self):
		pass

	def detect(self, instance, touch):
		#if not instance.collide_point(touch.x, touch.y):
		#	return False
		if touch.dx<-40:
			pass
		if touch.dx>40:
			pass
		if touch.dy<-40:
			pass
		if touch.dy>40:
			pass
		return True

if __name__=='__main__':
	SlideDetectApp().run()