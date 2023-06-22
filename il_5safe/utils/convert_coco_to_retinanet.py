import json
import os

def convert_annotations(annotations_file):
    with open(annotations_file) as file:
        data = json.load(file)

    annotations = {}

    for annotation in data['annotations']:
        image_id = annotation['image_id']
        file_name = next(image['file_name'] for image in data['images'] if image['id'] == image_id)
        category_id = annotation['category_id']
        category = next(category for category in data['categories'] if category['id'] == category_id)
        label = category['name']

        bbox = annotation['bbox']
        x, y, width, height = bbox
        box = [x, y, x + width, y + height]

        if file_name not in annotations:
            annotations[file_name] = {'labels': [], 'boxes': []}

        annotations[file_name]['labels'].append(label)
        annotations[file_name]['boxes'].append(box)

    return annotations


annotations_file = './../resources/coco_format/instances_default.json'
output_dir = './../resources/faster-rcnn_format/annotations_custom_try'

converted_data = convert_annotations(annotations_file)

os.makedirs(output_dir, exist_ok=True)

for file_id, annotation_data in converted_data.items():
    #file_name = '{:d}.json'.format(file_id)
    file_name = file_id + '.json'
    output_file = os.path.join(output_dir, file_name)
    with open(output_file, 'w') as file:
        json.dump(annotation_data, file)