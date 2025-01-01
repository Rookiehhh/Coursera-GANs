from bs4 import BeautifulSoup

# Read the HTML file
with open('D:/Desktop/AI/Coursera/GANs/GANS_C1/week1/index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract form details
form = soup.find('form')
form_action = form.get('action')
form_method = form.get('method')

# Extract input fields
username_input = form.find('input', {'name': 'username'})
password_input = form.find('input', {'name': 'password'})

# Extract alternative login buttons
buttons = soup.find_all('button')
button_links = [button.get('onclick').split("'")[1] for button in buttons]

# Print extracted information
print(f"Form Action: {form_action}")
print(f"Form Method: {form_method}")
print(f"Username Input: {username_input.get('name')}")
print(f"Password Input: {password_input.get('name')}")
print("Alternative Login Links:")
for link in button_links:
    print(link)