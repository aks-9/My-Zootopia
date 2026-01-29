import json


# Function to load JSON data
def load_data(file_path):
    """Loads a JSON file and returns the data"""
    with open(file_path, "r") as handle:
        return json.load(handle)


# Load animals data
animals_data = load_data('animals_data.json')

# Step 1: Read the template HTML
with open('animals_template.html', 'r') as template_file:
    html_template = template_file.read()

# Step 2: Generate the animals info string
animals_info = ""
for animal in animals_data:
    # Name
    if 'name' in animal:
        animals_info += f"Name: {animal['name']}<br>\n"

    # Diet
    diet = animal.get('characteristics', {}).get('diet')
    if diet:
        animals_info += f"Diet: {diet}<br>\n"

    # First location
    locations = animal.get('locations', [])
    if locations:
        animals_info += f"Location: {locations[0]}<br>\n"

    # Type
    animal_type = animal.get('characteristics', {}).get('type')
    if animal_type:
        animals_info += f"Type: {animal_type}<br>\n"

    # Add a line break between animals
    animals_info += "<br>\n"

# Step 3: Replace placeholder in template
final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

# Step 4: Write to a new HTML file
with open('animals.html', 'w') as output_file:
    output_file.write(final_html)

print("animals.html has been created successfully!")
