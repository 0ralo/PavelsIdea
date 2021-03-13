import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class MyGrid(GridLayout):
	pass


class OraliaApp(App):
	def build(self):
		global debil
		gl = MyGrid()
		bombs = []
		for i in range(20):
			bombs.append(random.randint(0, 20*20))
		for i in range(20):
			for j, k in zip(range(20), range(i * 20, i * 20 + 20)):
				button = Button(text="#")
				if k in bombs:
					button.bind(on_press=bomb)
					if debil:
						button.background_color = [1, 0, 0, 1]
					button.cords = [i, j]
					button.type = "bomb"
				else:
					button.bind(on_press=shown)
					button.cords = [i, j]
					button.type = "space"
				gl.add_widget(button)
		return gl


def bomb(self):
	self.background_color = [1, 0, 0, 1]
	for i in self.parent.children:
		if i.type == "bomb":
			i.background_color = [1, 0, 0, 1]
	self.parent.disabled = True


def shown(self):
	grid = self.parent
	Mycords = self.cords
	cords = []
	bombs = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			cords.append([Mycords[0] + i, Mycords[1] + j])
	for i in grid.children:
		if i.cords in cords:
			if i.type == "bomb":
				bombs += 1
	self.background_color = [0, 1, 0, 1]
	self.text = str(bombs)


if __name__ == '__main__':
	debil = True
	OraliaApp().run()
