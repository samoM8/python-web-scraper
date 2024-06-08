import requests
from bs4 import BeautifulSoup

def extract_customers(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    customers = []

    # Example for extracting from https://scale.com
    if "scale.com" in url:
        for img_tag in soup.find_all('img', {'class': 'client-logo'}):
            customer = {}
            customer['logo_url'] = img_tag['src']
            customer['name'] = img_tag.get('alt', 'N/A')
            customers.append(customer)

    # Example for extracting from https://deel.com
    elif "deel.com" in url:
        for div_tag in soup.find_all('div', {'class': 'client-logo'}):
            img_tag = div_tag.find('img')
            customer = {}
            customer['logo_url'] = img_tag['src']
            customer['name'] = img_tag.get('alt', 'N/A')
            customers.append(customer)

    # Example for extracting from https://webflow.com
    elif "webflow.com" in url:
        for img_tag in soup.find_all('img', {'class': 'customer-logo'}):
            customer = {}
            customer['logo_url'] = img_tag['src']
            customer['name'] = img_tag.get('alt', 'N/A')
            customers.append(customer)

    return customers

urls = [
    'https://scale.com',
    'https://deel.com',
    'https://webflow.com'
]

for url in urls:
    customers = extract_customers(url)
    with open(f"{url.split('//')[1].split('.')[0]}_customers.txt", 'w') as file:
        for customer in customers:
            file.write(f"Logo URL: {customer['logo_url']}\n")
            file.write(f"Name: {customer['name']}\n")
            file.write("\n")
