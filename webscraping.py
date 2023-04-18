import re
from bs4 import BeautifulSoup
import csv
import requests
url = 'https://www.jumia.co.ke/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
product_list = soup.find_all('article', class_='prd _fb col c-prd')
for product in product_list:
    product_name = product.find('a', class_='core')['title']
    brand_name = product.find('div', class_='mtop-2 brand').text.strip()
    price = product.find('div', class_='prc').text.strip().replace(',', '')
    discount = product.find('div', class_='tag _dsct _sm').text.strip()
    reviews_count = product.find('div', class_='rev').text.strip().split()[0].replace('(', '')
    rating = product.find('div', class_='stars _s').get('data-stars')
    product_data = [product_name, brand_name, price, discount, reviews_count, rating]
with open('jumia_products.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Brand Name', 'Price', 'Discount', 'Reviews Count', 'Rating'])
    writer.writerows(product_data)
for product in product_data:
    rating = float(product[5])
    reviews_count = int(product[4])
    
    # Add one positive and one negative review
    rating = (rating * reviews_count) + 1.0 

