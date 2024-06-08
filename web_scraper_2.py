from bs4 import BeautifulSoup
import requests

def scale_customers() -> None:
    url = "https://scale.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    customers = set()

    logos = soup.find("div", class_ = "relative hidden lg:block h-14")
    for logo in logos.find_all("img"):
        customer_name = logo["alt"].title()
        logo_url = url + logo["src"]
        customers.add(f"{customer_name},{logo_url}")

    logos = soup.find("div", class_ = "hidden md:block")
    for logo in logos.find_all("img"):
        customer_name = logo["alt"].title()
        logo_url = url + logo["src"]
        customers.add(f"{customer_name},{logo_url}")

    logos = soup.find("div", "w-full sm:flex items-center hidden grow min-h-[40px] mt-12 justify-evenly")
    for logo in logos.find_all("img"):
        customer_name = logo["alt"].title()
        logo_url = url + logo["src"]
        customers.add(f"{customer_name},{logo_url}")

    with open ("scale_customers.csv", "w") as file:
        for c in customers:
            file.write(c + "\n")


    url = "https://scale.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    customers = set()
    customer_elements = soup.find_all("img", class_=lambda t: t is not None and "logo" in t.lower())
    for customer_element in customer_elements:
        customer_name = customer_element["alt"].title()
        logo_url = url + customer_element["src"]
        customers.add(f"{customer_name},{logo_url}")

    with open ("scale_customers.csv", "w") as file:
        for c in customers:
            file.write(c + "\n")

    # Nevem a to lahko ali ne, da je iz /customers
    # url: str = "https://scale.com/customers"
    # r = requests.get(url)

    # soup = BeautifulSoup(r.content, "lxml")
    # customer_elements = soup.find("div", class_ = "ρi ρxV7Id")

    # with open("scale_customers_2.csv", "w") as file:
    #     for customer_element in customer_elements.find_all("img"):
    #         customer_name = customer_element["alt"]
    #         customer_url = "https://scale.com" + customer_element["src"]
    #         file.write(f"{customer_name},{customer_url}\n")

def deel_customers() -> None:
    """
    deel_customers extracts customer logos and names
    from webpage https://www.deel.com and writes them
    to a file
    """
    url = "https://www.deel.com"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    customer_elements = soup.find("div", class_ = "MuiBox-root css-3zzrsz")
    
    with open("deel_customers.csv", "w") as file:
        for customer_element in customer_elements.find_all("img"):
            logo_link = customer_element["src"]
            svg_name = logo_link.split("/")[-1]
            customer_name = svg_name[0: svg_name.rindex("_")].replace("_", " ").title()
            # print(f"{customer_name} {logo_link}")
            file.write(f"{customer_name},{logo_link}\n")

def webflow_customers() -> None:
    """
    webflow_customers extracts customer logos and names
    from webpage https://webflow.com and writes them
    to a file
    """
    url = "https://webflow.com"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    customer_elements = soup.find("section", class_ = "s")
    customers = set()
    with open("webflow_customers.csv", "w") as file:
        for customer_element in customer_elements.find_all("img"):
            logo_link = customer_element["src"]
            customer_name = customer_element["alt"][0: len(customer_element) - 5].title()

            if customer_name in customers:
                continue

            customers.add(customer_name)
            # print(f"{customer_name} {logo_link}")
            file.write(f"{customer_name},{logo_link}\n")

def main():
    scale_customers()
    deel_customers()
    webflow_customers()

if __name__ == "__main__":
    main()
