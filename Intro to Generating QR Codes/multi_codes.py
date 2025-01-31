import csv
import os
import datetime
import segno
import re

# Create the folder with the current date and time
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
folder_path = os.path.join("QR Codes", current_datetime)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Open the CSV file and read the URLs
urls = []
with open('urls.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        urls.append(row[0])

# Create QR codes for each URL and save them in the folder
failed_urls = []
file_names = []
for i, url in enumerate(urls, start=1):
    try:
        qr_code = segno.make_qr(url)

        # Extract the domain and path from the URL
        domain = re.sub(r'https?://www\.', '', url.split('/')[0])
        domain = re.sub(r'[^a-zA-Z0-9]', '', domain)
        path = url[len(domain)+len('://'):].replace('/', '_').replace('.', '_')

        # Generate a unique file name
        file_name = f"{domain}_{path}.png"

        # Check for duplicate file names and append a counter
        if file_name in file_names:
            counter = 2
            while f"{file_name[:-4]}_{counter}.png" in file_names:
                counter += 1
            file_name = f"{file_name[:-4]}_{counter}.png"
        file_names.append(file_name)

        file_path = os.path.join(folder_path, file_name)
        qr_code.save(
            file_path,
            scale=8,  # size
            border=2,
            # light="#ADD8E6",
            # dark="darkblue",
            # quiet_zone="maroon",
            # data_dark="green",
            # data_light="lightgreen",
        )
        print(f"QR Code for {url} saved successfully!")
    except Exception as e:
        print(f"Error creating QR code for {url}: {e}")
        failed_urls.append(url)

# Print the result message
if failed_urls:
    print("Some QR codes could not be created successfully:")
    for url in failed_urls:
        print(f"- {url}")
else:
    print("All QR codes created successfully!")

# RUN IN TERMINAL
# python multi_codes.py