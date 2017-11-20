class Surface(object):
	def __init__(self, tl, data):
		self.rect = Rect(tl, Size(len(data[0]), len(data)))
		self.data = data
	
	def draw(self, surface):
		for x in range(surface.rect.left, surface.rect.right):
			for y in range(surface.rect.top, surface.rect.bottom):
				self.data[y][x] = surface.data[y-surface.rect.top][x-surface.rect.left]


class Rect(object):
	def __init__(self,pos, size):
		self.width = size.width
		self.height = size.height
		
		self.tl = pos
		self.tr = Point(pos.x+self.width, pos.y)
		self.bl = Point(pos.x, pos.y + self.height)
		self.br = Point(pos.x + self.width, pos.y+ self.height)
	
		self.left = pos.x
		self.right = pos.x + self.width
		self.top = pos.y
		self.bottom = pos.y+ self.height

		self.center = Point((pos.x+self.width)/2, (pos.y+self.height)/2)
	
	def inRect(self,Point):
		if (self.left <= Point.x <= self.right) and (self.top <= Point.y <= self.bottom):
			return True
		return False

class Size(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height


class Point(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Text(Surface):
	def __init__(self, tl, text):
		Surface.__init__(self, tl, [list(text),[" " for i in range(len(text))]])
		self.text = text
	def highlight(self):
		for i in range(len(self.text)):
			self.data[1][i] = "-"
	def unhighlight(self):
		for i in range(len(self.text)):
			self.data[1][i] = " "

class Rectangle(Surface):
	def __init__(self, tl, size):
		data = [[" " for i in range(size.width)] for j in range(size.height)]
		for i in range(size.width):
			data[0][i] = "-"
			data[-1][i] = "-"
		for j in range(size.height):
			data[j][0] = "|"
			data[j][-1] = "|"
		Surface.__init__(self, tl, data)

class Paragraph(Surface):
	def __init__(self, tl, max_size, text):
		max_width = max_size.width
		data = []
		
		# Text Wrapping Mechanism
		for line in text.splitlines():
			while len(line) > max_width:
				max_line = line[:max_width]
				last_space_rev = max_line[-1::-1].find(" ")
				if last_space_rev == -1:
					last_space = max_width
					line = line[:max_width-1] + "-" + line[max_width-1:]
				else:
					last_space = len(max_line) - max_line[-1::-1].find(" ") - 1
				data.append(list(line[:last_space]) + [" " for i in range(max_width-last_space)])
				line = line[last_space:].lstrip()
			line_data = list(line) + [" " for i in range(max_width-len(line))]
			data.append(line_data)
		data = data[:max_size.height]
		Surface.__init__(self, tl, data)

class InputBox(Surface):
	def __init__(self, tl, width):
		data = [[" " for i in range(width)] for i in range(3)]
		for i in range(1,width-1):
			data[0][i] = "_"
			data[2][i] = "-"
		data[1][0] = "|"
		data[1][-1] = "|"
		self.text = ""
		self.max_text_len = width-2
		self.current_char = 1
		data[1][1] = "_"
		Surface.__init__(self, tl, data)
	def input(self, char):
		if (len(self.text) < self.max_text_len):
			self.text += char
			self.data[1][self.current_char] = char
			if (len(self.text) < self.max_text_len):
				self.current_char += 1
				self.data[1][self.current_char] = "_"
	def backSpace(self):
		if (len(self.text) > 0):
			self.data[1][self.current_char] = " "
			self.current_char -= 1
			self.data[1][self.current_char] = "_"
			self.text = self.text[:-1]
	def clearInput(self):
		for i in range(1, self.max_text_len+1):
			self.data[1][i] = " "
		self.text = ""
		self.current_char = 1
		self.data[1][1] = "_"