from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("product_details.html")

@app.route("/productsearch",methods = ["GET","POST"])
def profinfo():
    if request.method== "POST":
        inputs = request.form["search_pro"]   
        path = "C:/Users/Ganesh Mogaveera/Downloads/chromedriver-win64/chromedriver.exe"
        s = Service(path)
        driver = webdriver.Chrome(service = s)
        driver.get("https://www.ebay.com/")
        box = driver.find_element("xpath","/html/body/div[3]/div/div/div/div[1]/header/section/form/div[1]/div/div/input")
        box.send_keys(inputs,Keys.ENTER)
        section = driver.find_element("xpath","/html/body/div[5]/div[4]/div[3]/div[1]/div[3]")
        image = []
        images= section.find_elements("css selector","img[src]")
        for i in images:
            l=i.get_attribute("src")
            image.append(l)
        print(image) 
        
        shoes_name = section.find_elements("css selector",'[role="heading"]')
        shoes_heading = []
        for i in shoes_name:
            l = i.text
            shoes_heading.append(l)
          
    
        shoes_rate = section.find_elements("css selector",'[class="s-item__price"]')
        shoes_price = []
        for i in shoes_rate:
            l = i.text
            shoes_price.append(l)
        location_value = section.find_elements("css selector",'[class="s-item__location s-item__itemLocation"]')
        shoes_location = []
        for i in location_value:
            m = i.text
            shoes_location.append(m)
        mainl = [[image[i],shoes_heading[i],shoes_price[i],shoes_location[i]] for i in range(len(image))]
        # mainl.append(image)
        # mainl.append(shoes_heading)
        # mainl.append(shoes_price)
        # mainl.append(shoes_location)
        return render_template("product_details.html",online= mainl )
    else:
        return render_template("product_details.html")
    
        

if __name__ =="__main__":
    app.run(debug=True)

