import os
import xml.etree.ElementTree as ET


def convert_xml_to_yolo(xml_path, image_folder, output_folder, class_map):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    image_name = root.find('filename').text
    image_width = float(root.find('size/width').text)
    image_height = float(root.find('size/height').text)

    with open(os.path.join(output_folder, image_name.replace('png', 'txt')), 'w') as out_file:
        for obj in root.findall('object'):
            obj_name = obj.find('name').text
            class_id = class_map[obj_name]  # Map class name to class ID

            bndbox = obj.find('bndbox')
            x_min = float(bndbox.find('x').text)
            y_min = float(bndbox.find('y').text)
            x_max = x_min + float(bndbox.find('w').text)
            y_max = y_min + float(bndbox.find('h').text)

            x_center = ((x_min + x_max) / 2) / image_width
            y_center = ((y_min + y_max) / 2) / image_height
            width = (x_max - x_min) / image_width
            height = (y_max - y_min) / image_height

            out_file.write(f"{class_id} {x_center} {y_center} {width} {height}\n")


# Define paths
xml_folder = 'BoxAnnotations'
image_folder = 'Images'
output_folder = 'yolo_annotations1'

unique_classes =  ['Wall', 'Valve', 'Bottle', 'Hook', 'Propeller', 'Shampoo-bottle', 'Chain', 'Standing-bottle', 'Can', 'Drink-carton', 'Tire']

class_map = {name: idx for idx, name in enumerate(unique_classes)}

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)


# Convert all XML files to YOLO format
for xml_file in os.listdir(xml_folder):
    if xml_file.endswith('.xml'):
        xml_path = os.path.join(xml_folder, xml_file)
        convert_xml_to_yolo(xml_path, image_folder, output_folder, class_map)
