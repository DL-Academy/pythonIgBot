from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Getpages:
	def __init__(self, driver):
		self.driver = driver
		self.driver.get('https://www.instagram.com/python.learning')
		self.hrefs = []
	def get_num_flw(self):
		flw = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main')))
		sflw = b(flw.get_attribute('innerHTML'), 'html.parser')
		followers = sflw.findAll('span', {'class':'g47SY'})
		f = followers[1].getText().replace(',', '')
		if 'k' in f:
			f = float(f[:-1]) * 10**3
			return f
		elif 'm' in f:
			f = float(f[:-1]) * 10**6
			return f
		else:
			return float(f)

	def get_followers(self):
		time.sleep(2)
		flw_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > span')))
		flw_btn.click()
		time.sleep(3)
		self.popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]')))
		for h in range(11):
			time.sleep(1)
			print('scrolling')
			print(h)
			print('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)))
			self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)), self.popup)
			if h == 5:
				break
		for i in range(40):
			time.sleep(2)
			self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', self.popup)
		self.popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]')))
		b_popup = b(self.popup.get_attribute('innerHTML'), 'html.parser')
		for p in b_popup.findAll('li', {'class': 'wo9IH'}):
			try:
				hlink = p.find_all('a')[0]['href']
				print(hlink)
				if 'div' in hlink:
					print('div found not adding to list')
				else:
					self.hrefs.append(hlink)
			except:
				pass
		return self.hrefs
			
				

	def is_public(self):
		try:
			astate = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'rkEop')))
			if astate.text == 'This Account is Private':
				return False
			else:
				return True
		except:
			return True
	def like_post(self):
		post = self.driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1)')
		html = post.get_attribute('innerHTML')
		h = b(html, 'html.parser')
		href = h.a['href']
		self.driver.get('https://www.instagram.com' + href)
		like_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > span')))
		like_btn.click()
	def follow_page(self):
		follow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/button')))
		f_text = follow.text
		if f_text.lower() == 'follow' or f_text.lower() == 'follow back':
			follow.click()
		elif f_text == 'already following':
			print('already following')
		time.sleep(1)

