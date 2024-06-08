from bs4 import BeautifulSoup
import requests

page = requests.get("https://realpython.github.io/fake-jobs/")
# print(page.text)
# print(page.content)

# You’ll want to pass page.content instead of page.text to avoid problems 
# with character encoding. The .content attribute holds raw bytes, which 
# can be decoded better than the text representation you printed earlier 
# using the .text attribute.
soup = BeautifulSoup(page.content, "lxml")

results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()


python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

    link_url = job_element.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")

