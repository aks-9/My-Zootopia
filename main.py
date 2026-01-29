import json


# Function to load JSON data
def load_data(file_path):
    """Loads a JSON file and returns the data"""
    with open(file_path, "r") as handle:
        return json.load(handle)


# Load the animals data
animals_data = load_data('animals_data.json')

# Iterate through each animal and print required fields
for animal in animals_data:
    print()  # Blank line between animals
    # Name
    if 'name' in animal:
        print(f"Name: {animal['name']}")

    # Diet (nested inside 'characteristics')
    diet = animal.get('characteristics', {}).get('diet')
    if diet:
        print(f"Diet: {diet}")

    # First location
    locations = animal.get('locations', [])
    if locations:
        print(f"Location: {locations[0]}")

    # Type (nested inside 'characteristics')
    animal_type = animal.get('characteristics', {}).get('type')
    if animal_type:
        print(f"Type: {animal_type}")
