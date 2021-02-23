import requests
import csv

def get_page(text) :
    # get the next page value 

    r = text.split()
    page = r[len(r) - 1]
    return page 

def get_array(text) :
    # get array of two number : [No. , hex_value]

    r = text.split()
    
    first_number = r[0].replace("[","").replace(",","")
    second_number = r[1].split("\'")[1]
   
    array = [first_number, second_number]
    return array 
    
def get_response(url,page) :
    # get response from the given url and next page value

    new_url = url+page
    response = requests.get(new_url)
    return response

if __name__ == '__main__' :

    url = 'http://167.71.246.232:8080/rabbit_hole.php?page='
    page = 'cE4g5bWZtYCuovEgYSO1'
    response = get_response(url, page)
    
    #Using cvs file to write the array 
    with open('rabbit_hole.csv', 'w', newline = '') as csvfile :
        rabbit_csv = csv.writer(csvfile, delimiter=';', quotechar='|', quoting = csv.QUOTE_MINIMAL)
    
        while(response.text != 'end') :
            page = get_page(response.text)
            array = get_array(response.text)
            response = get_response(url, page)

            rabbit_csv.writerow(array)
