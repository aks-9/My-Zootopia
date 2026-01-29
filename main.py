import json


def load_data(file_path):
    """Loads a JSON file and returns the data."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serialize a single animal into an HTML <li> card."""
    output = '<li class="cards__item">\n'

    # Card title
    if 'name' in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    # Card text
    output += '  <p class="card__text">\n'

    # Diet
    diet = animal_obj.get('characteristics', {}).get('diet')
    if diet:
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'

    # First location
    locations = animal_obj.get('locations', [])
    if locations:
        output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'

    # Type
    animal_type = animal_obj.get('characteristics', {}).get('type')
    if animal_type:
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

    return output


def generate_animals_html(data):
    """Generate the full HTML string for all animals."""
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output


def main():
    # Load data
    animals_data = load_data('animals_data.json')

    # Read template
    with open('animals_template.html', 'r') as template_file:
        html_template = template_file.read()

    # Generate animal cards HTML
    animals_info = generate_animals_html(animals_data)

    # Replace placeholder in template
    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    # Write final HTML file
    with open('animals.html', 'w') as output_file:
        output_file.write(final_html)

    print("animals.html has been created successfully!")


if __name__ == "__main__":
    main()
