import os
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service


webdriver_path = "C:/Users/Home/OneDrive/Desktop/msedgedriver.exe"
service = Service(webdriver_path)


search_queries = [
"Python programming",
"How to bake a cake",
"Latest news",
"Best movies 2024",
"Weather today",
"Top tech gadgets",
"Learn Spanish online",
"Workout routines",
"Travel destinations",
"History of the internet",
"GitHub",
"Quora",
"Discord",
"JavaScript tutorials",
"Vegan recipes",
"Breaking news",
"Upcoming movies",
"Weather tomorrow",
"Smart home devices",
"Learn French online",
"Yoga exercises",
"European travel",
"Invention of the computer",
"Stack Overflow",
"Reddit",
"Slack",
"Java programming",
"Keto diet recipes",
"World news",
"Top TV shows 2024",
"Weather forecast",
"Wearable tech",
"Learn German online",
"Cardio workouts",
"Beach destinations",
"Evolution of smartphones",
"Bitbucket",
"Medium",
"Telegram",
"C++ programming",
"Gluten-free recipes",
"Technology news",
"Box office hits",
"Weekend weather",
"Gaming consoles",
"Learn Italian online",
"Strength training",
"Mountain getaways",
"History of social media",
"Hacker News",
"Medium articles",
"Trello",
"HTML tutorials",
"Paleo diet recipes",
"National news",
"Top podcasts 2024",
"Weather radar",
"Virtual reality headsets",
"Learn Japanese online",
"HIIT workouts",
"City breaks",
"Milestones of the internet",
"SourceForge",
"Dev.to",
"Basecamp",
"Ruby programming",
"Low-carb recipes",
"Political news",
"Oscar nominations 2024",
"Weather alerts",
]


driver = webdriver.Edge(service=service)


def perform_random_search():
    search_query = random.choice(search_queries)
    driver.get("https://www.bing.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(random.uniform(2, 5))  

try:
    
    for _ in range(20):  
        perform_random_search()
        time.sleep(random.uniform(5, 10)) 

finally:
    
    driver.quit()



    