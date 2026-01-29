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

# Step 2: Generate the animals info string as HTML <li> cards
animals_info = ""
for animal in animals_data:
    animals_info += '<li class="cards__item">\n'

    # Card title
    if 'name' in animal:
        animals_info += f'  <div class="card__title">{animal["name"]}</div>\n'

    # Card text
    animals_info += '  <p class="card__text">\n'

    # Diet
    diet = animal.get('characteristics', {}).get('diet')
    if diet:
        animals_info += f'      <strong>Diet:</strong> {diet}<br/>\n'

    # First location
    locations = animal.get('locations', [])
    if locations:
        animals_info += f'      <strong>Location:</strong> {locations[0]}<br/>\n'

    # Type
    animal_type = animal.get('characteristics', {}).get('type')
    if animal_type:
        animals_info += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    animals_info += '  </p>\n'  # Close card text
    animals_info += '</li>\n'  # Close card item

# Step 3: Replace placeholder in template
final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

# Step 4: Write to a new HTML file
with open('animals.html', 'w') as output_file:
    output_file.write(final_html)

print("animals.html has been created successfully!")
