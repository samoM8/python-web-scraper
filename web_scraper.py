from bs4 import BeautifulSoup
import requests

def scale_customers() -> None:
    """
    scale_customers extracts customer logos and names from 
    webpage https://www.scale.com and writes them to a file
    """
    url = "https://scale.com/"
    r = requests.get(url)
    if r.status_code != 200:
        print(f"Failed to retrieve data from {url}. Status code: {r.status_code}")
        return None
    
    soup = BeautifulSoup(r.content, "lxml")

    customers = set()
    customer_elements = soup.find_all("img", class_ = lambda x: x is not None and "logo" in x.lower())
    for customer_element in customer_elements:
        customer_name = customer_element["alt"].title()
        logo_url = url + customer_element["src"]
        customers.add(f"{customer_name},{logo_url}")

    customer_elements = soup.find("div", "w-full sm:flex items-center hidden grow min-h-[40px] mt-12 justify-evenly")
    i = 0
    for customer_element in customer_elements.find_all("img"):
        customer_name = customer_element.parent.parent.parent \
                        .find_all("p", class_ = "text-base text-white text-opacity-75")[i] \
                        .text.split(", ")[-1]
        i += 1
        logo_link = url + customer_element["src"]
        customers.add(f"{customer_name},{logo_link}")

    with open("scale_customers.csv", "w") as file:
        for c in customers:
            file.write(c + "\n")

def deel_customers() -> None:
    """
    deel_customers extracts customer logos and names from
    webpage https://www.deel.com and writes them to a file
    """
    url = "https://www.deel.com"
    r = requests.get(url)
    if r.status_code != 200:
        print(f"Failed to retrieve data from {url}. Status code: {r.status_code}")
        return None

    soup = BeautifulSoup(r.content, "lxml")

    customer_elements = soup.find("div", class_ = "MuiBox-root css-3zzrsz")
    with open("deel_customers.csv", "w") as file:
        for customer_element in customer_elements.find_all("img"):
            logo_link = customer_element["src"]
            svg_name = logo_link.split("/")[-1]
            customer_name = svg_name[0: svg_name.rindex("_")].replace("_", " ").title()
            file.write(f"{customer_name},{logo_link}\n")

def webflow_customers() -> None:
    """
    webflow_customers extracts customer logos and names from
    webpage https://webflow.com and writes them to a file
    """
    url = "https://webflow.com"
    r = requests.get(url)
    if r.status_code != 200:
        print(f"Failed to retrieve data from {url}. Status code: {r.status_code}")
        return None
    
    soup = BeautifulSoup(r.content, "lxml")

    customers = set()
    customer_elements = soup.find_all("img", alt = lambda x: x is not None and "logo" in x.lower())
    for customer_element in customer_elements:
        customer_name = customer_element["alt"][0: len(customer_element)-5].title()
        logo_url = customer_element["src"]
        customers.add(f"{customer_name},{logo_url}")

    with open("webflow_customers.csv", "w") as file:
        for c in customers:
            file.write(c + "\n")

def main():
    scale_customers()
    deel_customers()
    webflow_customers()

if __name__ == "__main__":
    main()
