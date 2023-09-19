from Nonogram import *
from threading import Thread

def renderIndications(row_list, col_list):
	rowThread = Thread(target=putRowNums, args=(row_list,))
	rowThread.start()
	colThread = Thread(target=putColNums, args=(col_list,))
	colThread.start()

	rowThread.join()
	colThread.join() 

def putRowNums(row_list):

	pygame.init()
	font = pygame.font.SysFont('ptmono.ttf', 40)

	for x in range(len(row_list)):
		nums = str(row_list[x])
		nums = nums.replace(', ', ' ')

		# create a text surface object,
		# on which text is drawn on it.
		text = font.render(nums[1:-1], True, white, gray)

		# create a rectangular object for the
		# text surface object
		textRect = text.get_rect()

		# set the center of the rectangular object.
		textRect.center = (VARS['grid_Origin'][0] // 2, (VARS['grid_Origin'][1] + 25) + 50 * x)
		#place object(text) on the board
		VARS['board'].blit(text, textRect)

def putColNums(col_list):

	pygame.init()
	font = pygame.font.SysFont('ptmono.ttf', 40)

	for x in range(len(col_list)):
		nums = str(col_list[x])
		nums = nums.replace(', ', ' ')

		text = font.render(nums[1:-1], True, white, gray)
		text = pygame.transform.rotate(text, 270)

		textRect = text.get_rect()

		textRect.center = ((VARS['grid_Origin'][0] + 25) + 50 * x, VARS['grid_Origin'][1]/2)
		VARS['board'].blit(text, textRect)