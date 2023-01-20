# import urllib
# use urllib.request to get the data from the url
# write a fucntion that takes a url
# return a response

import urllib.request as urllib


def main(url):
     print("CHecking connectivity   ")

     response = urllib.urlopen(url)
     print("Connected to", url, "successfully")
     print("The response code was:", response.getcode())

     
print("This is a site connectivity checker")
input_url = input("Input the url of the site you want to check:")



main(input_url) 






