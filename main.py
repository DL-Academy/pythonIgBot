from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import login
import getpages 

username = 'username'
password = 'password'
driver = 0
refs = []
max_likes = 350
max_follows = 50

def main():
	global driver
	print('running script..')
	driver = webdriver.Chrome('C://Users/Ryan/Desktop/chromedriver.exe')
	l = login.Login(driver, username, password)
	l.signin()
	gp = getpages.Getpages(driver)
	refs = gp.get_followers()
	print(gp.get_num_flw())
	run_bot(refs, driver, gp)
	
def run_bot(refs, driver, gp):
	print(len(refs))
	print('accounts targeted')
	t = time.time()
	#how many pages we likes / followed
	L = 0
	F = 0
	for r in refs:
		driver.get('https://www.instagram.com' + r)
		time.sleep(2)
		if gp.get_num_flw() < 3000:
			if gp.is_public():
				print('public account')
				print('current likes: ' + str(L))
				if L < max_likes:
					try:
						gp.like_post()
						L += 1
						print("POST LIKED")
					except:
						print('could not like..lets follow instead')
						try:
							gp.follow_page()
							print('page followed successfully')
							F += 1
						except:
							print('could not follow')
				else:
					time.sleep(3600) # time.sleep(3600 - (time.time() - t)) -> t= time.time()
			else:
				print('account is private')
				print('current follows: ' + str(F))
				if F < max_follows:
					time.sleep(2)
					try:
						gp.follow_page()
						print('page followed successfully')
						F += 1
					except:
						print('could not follow')
					
				else:
					time.sleep(3600)



if __name__ == '__main__':
	main()	