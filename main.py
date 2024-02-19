import requests 

def convert_currency():
    initial_currency = input("Enter the starting currency: ")
    target_currency = input("Enter the target currency: ")

    while True:
        try: 
            amount = float(input('Enter the amount: '))
        except:
            print("The amount needs to be a number.")
            continue

        if not amount > 0:
            print("Amount needs to be greater than 0.")
            continue

        else:
            break 


    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={initial_currency}&amount={amount}"

    payload = {}
    headers= {
            "apikey": "<api key>"
            }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    if status_code != 200:
        result = response.json()
        print("Error response: " + str(result))
        quit()
    
    #result = response.text
    result = response.json()
    print("Result = " + str(result['result']))

if __name__ == '__main__':
    convert_currency()


    
    