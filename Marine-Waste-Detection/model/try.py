# classes = ["wall", "bottle", "can","carton","box","bidon","pipe","platform","propeller","sachet","tire", "valve", "wrench","plastic","metal", "rubber","glass", "cardboard", "platform", "drink-sachet", "plastic-bidon", "plastic-bottle", "plastic-pipe", "plastic-propeller", "can", "metal-bottle", "metal-box", "valve", "wrench", "large-tire", "small-tire", "brown-glass-bottle", "glass-bottle", "glass-jar", "potion-glass-bottle", "drink-carton","rotating-platform", "plastic-bottle", "metal-bottle", "glass-bottle", "potion-glass-bottle", "drink-carton", "metal-box", "plastic-bidon", "plastic-pipe", "rotating-platform","plastic-propeller", "drink-sachet", "large-tire", "small-tire"]

# print("len of original",len(classes))

# unique_classes = list(set(classes))

# print("len of original",len(unique_classes))
# print(unique_classes)

# # unique_classes =  ['tire', 'wrench', 'small-tire', 'wall', 'glass-jar', 'bottle', 'glass', 'propeller', 'bidon', 'plastic', 'drink-carton', 'metal-bottle', 'valve', 'potion-glass-bottle', 'large-tire', 'metal', 'brown-glass-bottle', 'rubber', 'plastic-bottle', 'plastic-bidon', 'box', 'drink-sachet', 'metal-box', 'plastic-propeller', 'plastic-pipe', 'rotating-platform', 'pipe', 'carton', 'cardboard', 'can', 'glass-bottle', 'platform', 'sachet']
import os
import xml.etree.ElementTree as ET

def collect_class_names(xml_folder):
    class_names = set()  # Use a set to avoid duplicates

    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith('.xml'):
            xml_path = os.path.join(xml_folder, xml_file)
            tree = ET.parse(xml_path)
            root = tree.getroot()

            for obj in root.findall('object'):
                class_name = obj.find('name').text
                class_names.add(class_name)  # Add class name to the set

    return list(class_names)  # Convert set back to list for further processing

# Define path to the XML folder
xml_folder = 'BoxAnnotations'

# Collect all class names from XML files
unique_class_names = collect_class_names(xml_folder)

# Print the collected class names
print("Unique class names:", unique_class_names)


