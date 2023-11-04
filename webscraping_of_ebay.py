import requests
from bs4 import BeautifulSoup
import pandas as pd
from google.colab import files

# Initialize empty lists for name and price
name = []
price = []

# Loop through the eBay pages
for i in range(2, 10):
    url = 'https://www.amazon.com/s?k=laptop&page=3&qid=1699072506&ref=sr_pg_{}'.format(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and collect name and price data
    for item in soup.find_all('div', class_='a-section'):
        name_elem = item.find('span', class_='a-size-medium a-color-base a-text-normal')
        price_elem = item.find('span', class_='a-price-whole')
        print(name_elem)

        # Check if both name and price elements exist
        if name_elem and price_elem:
            name.append(name_elem.text.strip())
            price.append(price_elem.text.strip())
        else:
            # Handle the case where name or price data is missing
            if name_elem:
                name.append(name_elem.text.strip())
                price.append(None)
            elif price_elem:
                name.append(None)
                price.append(price_elem.text.strip())

# Create a DataFrame
data = {'Name': name, 'Price': price}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
file_name = 'ebay_laptops_data.xlsx'
df.to_excel(file_name, index=False)

# Download the Excel file
files.download(file_name)

# Display the first few rows of the DataFrame
df.head()
