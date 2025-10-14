import requests
import xml.etree.ElementTree as ET
import csv

# RSS feed URL for daily rainfall data
RSS_URL = "https://data.gov.hk/filestore/feeds/data_rss_en.xml"

# Fetch the RSS feed
response = requests.get(RSS_URL)
response.raise_for_status()
xml_content = response.content

# Parse the XML
root = ET.fromstring(xml_content)

# Find all links to data files
links = []
for item in root.findall('.//item'):
    link = item.find('link')
    if link is not None and link.text.endswith('.csv'):
        links.append(link.text)

# Download the first CSV file found (for demo purposes)
if links:
    csv_url = links[0]
    print(f"Downloading: {csv_url}")
    csv_response = requests.get(csv_url)
    csv_response.raise_for_status()
    with open("rainfall_data.csv", "wb") as f:
        f.write(csv_response.content)
    print("Saved as rainfall_data.csv")
else:
    print("No CSV links found in the RSS feed.")
