import math
fout = open("pic.ppm","w")
size = 500
fout.write("P3\n"+str(size)+" "+str(size)+"\n255\n")


pixels = []
for i in range(size):
    pixels.append([])
    for j in range(size):
        pixels[i].append([0,0,0])

def draw_line(x0, y0, x1, y1, screen, r, g, b):
	#print("Drawing line from (" + str(x0) + ", " + str(y0) + ") to (" + str(x1) + ", " + str(y1) + ") with RGB " + str(r) + " " + str(g) + " " + str(b))
	if(x0 > x1): #octants 3 through 6
		draw_line(x1, y1, x0, y0, screen, r, g, b)
		return
	if(x0 == x1 and y0 > y1):
		draw_line(x1, y1, x0, y0, screen, r, g, b)
	if(y1 - y0 <= x1 - x0 and y1 - y0 >= 0): #octant 1
		x = x0
		y = y0
		A = y1 - y0
		B = x0 - x1
		d = 2*A + B
		while(x <= x1):
			#print("Plotting (" + str(x) + ", " + str(y) + ")")
			plot(screen, r, g, b, x, y)
			if(d > 0):
				y += 1
				d += 2*B
			x += 1
			d += 2*A
			#print(x, y, d)
	elif(y1 - y0 <= x1 - x0 and y1 - y0 < 0): #octant 8
		x = x0
		y = -1 * y0
		A = y0 - y1
		B = x0 - x1
		d = 2*A + B
		while(x <= x1):
			#print("Plotting (" + str(x) + ", " + str(-1 * y) + ")")
			plot(screen, r, g, b, x, -1 * y)
			if(d > 0):
				y += 1
				d += 2*B
			x += 1
			d += 2*A
	elif(y1 - y0 >= x1 - x0): #octant 2
		x = y0
		y = x0
		A = x1 - x0
		B = y0 - y1
		d = 2*A + B
		while(x <= y1):
			#print("Plotting (" + str(y) + ", " + str(x) + ")")
			plot(screen, r, g, b, y, x)
			if(d > 0):
				y += 1
				d += 2*B
			x += 1
			d += 2*A
	elif(y1 - y0 < x0 - x1): #octant 7
		x = -1*y0
		y = x0
		A = x1 - x0
		B = y1 - y0
		d = 2*A + B
		while(x <= -1*y1):
			#print("Plotting (" + str(-1*y) + ", " + str(x) + ")")
			plot(screen, r, g, b, y, x)
			if(d > 0):
				y += 1
				d += 2*B
			x += 1
			d += 2*A

def plot(screen, r, g, b, x, y):
	if(x < 0):
		plot(screen, r, g, b, 0, y)
		return
	if(x > 499):
		plot(screen, r, g, b, 499, y)
		return
	if(y < 0):
		plot(screen, r, g, b, x, 0)
		return
	if(y > 499):
		plot(screen, r, g, b, x, 499)
		return
	screen[499 - y][x][0] = r
	screen[499 - y][x][1] = g
	screen[499 - y][x][2] = b

XRES = 500
YRES = 500

#draw_line(0, 0, XRES-1, YRES-1, pixels, 0, 255, 0)
#draw_line(0, 0, XRES-1, YRES // 2, pixels, 0, 255, 0) 
#draw_line(XRES-1, YRES-1, 0, YRES // 2, pixels, 0, 255, 0)

#octants 8 and 4
#draw_line(0, YRES-1, XRES-1, 0, pixels, 0, 0, 255) 
#draw_line(0, YRES-1, XRES-1, YRES//2, pixels, 0, 0, 255)
#draw_line(XRES-1, 0, 0, YRES//2, pixels, 0, 0, 255)

#octants 2 and 6
#draw_line(0, 0, XRES//2, YRES-1, pixels, 255, 0, 0)
#draw_line(XRES-1, YRES-1, XRES//2, 0, pixels, 255, 0, 0)

#octants 7 and 3
#draw_line(0, YRES-1, XRES//2, 0, pixels, 255, 0, 255)
#draw_line(XRES-1, 0, XRES//2, YRES-1, pixels, 255, 0, 255)

#horizontal and vertical
#draw_line(0, YRES//2, XRES-1, YRES//2, pixels, 255, 255, 0)
#draw_line(XRES//2, 0, XRES//2, YRES-1, pixels, 255, 255, 0)

class Turtle:

	def __init__(self, myscreen, x0=XRES//2, y0=YRES//2, head=0, R=0, G=0, B=0):
		self.x = x0
		self.y = y0
		self.heading = head
		self.screen = myscreen
		self.r=R
		self.g=G
		self.b=B
		self.pendown = False
		self.stepcount = 0

	def pd(self):
		self.pendown = not(self.pendown)

	def setcolor(self, newr, newg, newb):
		self.r = newr
		self.g = newg
		self.b = newb

	def fd(self, length):
		newx = (self.x + length * math.sin(math.pi * self.heading / 180))
		newy = (self.y + length * math.cos(math.pi * self.heading / 180))
		intx = (int) (self.x + length * math.sin(math.pi * self.heading / 180))
		inty = (int) (self.y + length * math.cos(math.pi * self.heading / 180))
		goodx = (int) (self.x + 0.0)
		goody = (int) (self.y + 0.0)
		#print("Moving from (" + str(self.x) + ", " + str(self.y) + ") to (" + str(newx) + ", " + str(newy) + ")")
		if(self.pendown):
			draw_line(goodx, goody, intx, inty, self.screen, self.r, self.g, self.b)
		self.x = newx
		self.y = newy

	def setxy(self, newx, newy):
		self.x = newx
		self.y = newy

	def rt(self, angle):
		self.heading += angle

	def lt(self, angle):
		self.heading -= angle

	def movea(self, depth, initialdepth, sidelength):
		if(depth == 0):
			return
		else:
			self.lt(90)
			self.moveb(depth - 1, initialdepth, sidelength)
			self.fd(sidelength)
			self.stepcount += 1
			self.adjustcolor(self.stepcount, initialdepth)
			self.rt(90)
			self.movea(depth - 1, initialdepth, sidelength)
			self.fd(sidelength)
			self.stepcount += 1
			self.adjustcolor(self.stepcount, initialdepth)
			self.movea(depth - 1, initialdepth, sidelength)
			self.rt(90)
			self.fd(sidelength)
			self.stepcount += 1
			self.adjustcolor(self.stepcount, initialdepth)
			self.moveb(depth - 1, initialdepth, sidelength)
			self.lt(90)

	def moveb(self, depth, initialdepth, sidelength):
		if(depth == 0):
			return
		else:
			self.rt(90)
			self.movea(depth - 1, initialdepth, sidelength)
			self.fd(sidelength)
			self.stepcount += 1
			self.adjustcolor(self.stepcount, initialdepth)
			self.lt(90)
			self.moveb(depth - 1, initialdepth, sidelength)
			self.fd(sidelength)
			self.stepcount += 1
			self.adjustcolor(self.stepcount, initialdepth)
			self.moveb(depth - 1, initialdepth, sidelength)
			self.lt(90)
			self.fd(sidelength)
			self.stepcount += 1
			self.adjustcolor(self.stepcount, initialdepth)
			self.movea(depth - 1, initialdepth, sidelength)
			self.rt(90)

	def adjustcolor(self, stepcount, depth):
		totalsteps = 4**depth - 1
		self.r = (int)(128 * math.sin(2 * stepcount * math.pi / totalsteps) + 128)
		self.g = (int)(128 * math.sin(-1 * 2 * math.pi / 3 + 2 * stepcount * math.pi / totalsteps) + 128)
		self.b = (int)(128 * math.sin(-2 * 2 * math.pi / 3 + 2 * stepcount * math.pi / totalsteps) + 128)
		#print("RGB is " + str(self.r) + " " + str(self.g) + " " + str(self.b))

def hilbert(depth, screen):
	    gustavo = Turtle(pixels, 0, 0, 0, 0, 0)
	    sidelength = XRES / 2**depth
	    gustavo.setcolor(128, 0, 0)
	    gustavo.fd(sidelength / 2)
	    gustavo.rt(90)
	    gustavo.fd(sidelength / 2)
	    gustavo.pd()
	    gustavo.movea(depth, depth, sidelength)

hilbert(8, pixels)

for i in range(size):
    for j in range(size):
        fout.write(str(pixels[i][j][0])+" "+str(pixels[i][j][1])+" "+str(pixels[i][j][2])+" ")

    fout.write("\n")