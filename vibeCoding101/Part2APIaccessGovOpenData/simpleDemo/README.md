# README: How to Retrieve Hong Kong Daily Total Rainfall Data via API

## What Data Is Available
- Daily total rainfall records for Hong Kong
- Data is updated regularly and accessible via RSS (XML format)
- RSS feed lists new or updated data files from the past 14 days

## API Access
- Main API endpoint for the RSS feed:
  ```
  https://data.gov.hk/filestore/feeds/data_rss_en.xml
  ```
- Subscribe to this RSS feed using any RSS reader or fetch it programmatically

## How to Get the Data (Step-by-Step for Non-Programmers)
1. **Open the RSS Feed in Your Browser**
   - Go to: https://data.gov.hk/filestore/feeds/data_rss_en.xml
   - You will see a list of data files in XML format
2. **Use an RSS Reader**
   - Copy the RSS URL above and add it to your favorite RSS reader
   - The reader will show you new and updated rainfall data files
3. **Download Data Files**
   - In the XML, look for `<link>` tags. These are URLs to the actual data files
   - Click or copy these links to download the data

## Pseudo Code Example
```
1. Go to the RSS feed URL in your browser
2. Look for links to data files in the XML
3. Download the files you need
```
Or, for those comfortable with simple scripts:
```
Fetch the RSS feed from the URL
For each <link> in the XML:
    Download the file at that link
```

---
This guide explains how to access and download Hong Kong daily rainfall data using the official government API and RSS feed.
