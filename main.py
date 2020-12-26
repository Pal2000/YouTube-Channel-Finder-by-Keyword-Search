# Youtube Channel Finder by Keyword Search

from selenium import webdriver  # selenium use webdriver needs for cross-browser testing to ensure that it perform exceptedly
import time

baseUrl = "https://youtube.com/"
keyword = input("Enter the keyword : ")
  
def getChannelUrl():                               # Fetch all videos links matches with keyword
    s=baseUrl+"/search?q="+keyword
    driver.get(s)
    time.sleep(3)
    allChannelList= driver.find_elements_by_css_selector("#text.style-scope.ytd-channel-name a.yt-simple-endpoint.style-scope.yt-formatted-string")
    links = list(dict.fromkeys(map(lambda a: a.get_attribute("href"),allChannelList)))
    return links

def getChannelDetails(urls):                    # Move and show all matched YT channels and fetch all details of that channels
    details = []
    for url in urls:
        s=url+"/about"
        driver.get(s)    # data we get after visiting each and every channel
        cname = driver.find_element_by_css_selector("#text.style-scope.ytd-channel-name").text
        cDess = driver.find_element_by_css_selector("#description-container > yt-formatted-string:nth-child(2)").text
        clink = url
        csub = driver.find_element_by_css_selector("#subscriber-count").text
        cviews=driver.find_element_by_css_selector("#right-column > yt-formatted-string:nth-child(3)").text
        
        obj = {
            "cname" : cname,
            "curl"  : clink,
            "cdesc" : cDess,
            "csub" :csub,
            "cviews":cviews
        }
        details.append(obj)
    return details
if __name__ == "__main__":
    driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")       
    # path is needed for helping the webdriver so that it can locate the downloaded chrome webdriver ececutable file
    driver.implicitly_wait(5)
    allChannelUrls = getChannelUrl()
    allChannelDetails = getChannelDetails(allChannelUrls)
    for channel in allChannelDetails:
        print("Channel Name:=  " + channel["cname"])
        print()
        print("Channel Link:=  " + channel["curl"])
        print()
        print("No. of Subscribers:=  " + channel["csub"])
        print()
        print("Channel Description:=  " + channel["cdesc"])
        print()
        print("Total No. of views:=  " + channel["cviews"])
        print("")
        print("")
        print("")
        print("***************************************************************************************************")
        print()
        print()
            
    driver.close()
