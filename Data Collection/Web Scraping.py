import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

#Creating empty lists with the feature names, where the data is collected
Product_name = []
After_Discount_Price = []
Description = []
RAM = []
ROM = []
Rear_camera = []
Front_camera = []
Display_size = []
Battery_Capacity = []
Processor_Type = []
Image = []

#Scraping the data of these brand smartphones as these are most commonly seen these days.
Brands = ['SAMSUNG','APPLE','realme','POCO','OPPO','vivo','REDMI','MOTOROLA','Mi','REDMI','Nokia','IQOO','OnePlus']

#Iterating the loop brand-wise
for b in Brands:
    
    #Scraping the data of 2 pages from each brand 
    for i in range(1,3):
        
        url = 'https://www.flipkart.com/search?q=mobiles+under+30000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&p%5B%5D=facets.brand%255B%255D%3D{}&page='.format(b) + str(i)

        open_url = requests.get(url)

        soup = BeautifulSoup(open_url.text,'lxml')

        section = soup.find('div',class_='_1YokD2 _3Mn1Gg')

        names = section.find_all("div",class_='_4rR01T')

        for j in names:
            Product_name.append(j.text)

        adp = section.find_all('div',class_='_30jeq3 _1_WHN1')

        for k in adp:
            After_Discount_Price.append(k.text)

        imgs = section.find_all('img',class_='_396cs4')

        for i in imgs:
            Image.append(i['src'])

        des = section.find_all('div',class_='fMghEO')

        temp = []
        for m in des:
            temp.append(m.text)

        for n in temp:    
            # Define regular expressions patterns for extracting information
            ram_pattern = r'(\d+ [GM]B) RAM'
            rom_pattern = r'(\d+ [GM]B) ROM'
            battery_pattern = r'(\d+ mAh) Battery'
            front_cam_pattern = r'(\d+MP) Front Camera'
            rear_cam_pattern = r'(\d+MP \+ \d+MP)'
            processor_pattern = r'Battery(.+?)Processor'
            display_size_pattern = r'([\d.]+) inch'

            # Extract RAM information
            ram_match = re.search(ram_pattern,n)
            ram = ram_match.group(1) if ram_match else None

            # Extract ROM information
            rom_match = re.search(rom_pattern,n)
            rom = rom_match.group(1) if rom_match else None

            # Extract Battery information
            battery_match = re.search(battery_pattern,n)
            battery = battery_match.group(1) if battery_match else None

            # Extract Camera information
            camera_front_match = re.search(front_cam_pattern,n)
            camera_front = camera_front_match.group(1) if camera_front_match else None

            camera_rear_match = re.search(rear_cam_pattern,n)
            camera_rear = camera_rear_match.group(1) if camera_rear_match else None

            # Extract Processor information
            processor_match = re.search(processor_pattern,n)
            processor = processor_match.group(1) if processor_match else None

            # Extract display size
            display_size_match = re.search(display_size_pattern, n)
            display_size = display_size_match.group(1) if display_size_match else None

            RAM.append(ram)
            ROM.append(rom)
            Battery_Capacity.append(battery)
            Rear_camera.append(camera_rear)
            Front_camera.append(camera_front)
            Processor_Type.append(processor)
            Display_size.append(display_size)

#Creating a dataframe to store the data that we just scraped from the web page.
df = pd.DataFrame({'Product_name':Product_name,
             'After_Discount_Price':After_Discount_Price,
             'Product_Image':Image,
             'RAM':RAM,
             'ROM':ROM,
             'Front_camera':Front_camera,
             'Rear_camera':Rear_camera,
             'Battery_Capacity':Battery_Capacity,
             'Display_size':Display_size,
             'Processor':Processor_Type})

df.to_csv('smartphones.csv',index=False)

df

