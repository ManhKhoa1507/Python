import requests
import re


def get_key(text) : 
    r = re.split("\s",text)
    key = r[len(r) - 1] 
    return key

def get_response(url,i) :
    new_url = url+key
    response = requests.get(new_url)
    return response


if __name__ == '__main__' :

    url = 'http://167.71.246.232:8080/rabbit_hole.php?page='
    key = '4O48APmBiNJhZBfTWMzD'
    
    n = int(input())
    for i in range(n) : 
        response = get_response(url, key)
        
        if(response.status_code == 200) :
            key = get_key(response.text)
            print(i,':   ',key)
            
            if(key == 'cE4g5bWZtYCuovEgYS01') :
                tmp = repsonse.text
                break;
                print(tmp)
        else : 
            print('Not response')

