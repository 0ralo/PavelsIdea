import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class MyGrid(GridLayout):
	pass


class OraliaApp(App):
	def build(self):
		gl = MyGrid()
		j = random.randint(0, 20*20)
		for i in range(20*20):
			button = Button(text="#")
			if i == j:
				button.bind(on_press=secret)
			else:
				button.bind(on_press=hide)
			gl.add_widget(button)
		print(j)
		return gl


def hide(self):
	self.opacity = 0


def secret(self):
	grid = self.parent.parent.children[0]
	for i in grid.children:
		if i == self:
			i.text = "YOU WON"
		else:
			i.opacity = 0


if __name__ == '__main__':
	OraliaApp().run()
