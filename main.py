import urllib.request as urllib

def main(url):

    response = urllib.urlopen(url)
    print("the response code = ",response.getcode())


url = input("Enter The URL: ")
main(url)