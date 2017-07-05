import os
import io
import json
import hashlib

from PIL import Image
import tensorflow as tf

def create_example(img_dir, class_name, class_index, filename):
    img_path = os.path.join(img_dir, class_name, filename)
    with open(img_path[:-3] + 'json') as json_file:
        data = json.load(json_file)
    with open(img_path, 'rb') as img_file:
        encoded_jpeg = img_file.read()
    image = Image.open(io.BytesIO(encoded_jpeg))
    key = hashlib.sha256(encoded_jpeg).hexdigest()
    width, height = image.size
    xmin = data['xmin'] / width
    ymin = data['ymin'] / height
    xmax = data['xmax'] / width
    ymax = data['ymax'] / height
    truncated = 0
    poses = ''
    difficult_obj = 0
    return tf.train.Example(features=tf.train.Features(feature={
        'image/height': int64_feature(height),
        'image/width': int64_feature(width),
        'image/filename': bytes_feature(filename.encode()),
        'image/source_id': bytes_feature(filename.encode()),
        'image/key/sha256': bytes_feature(key.encode()),
        'image/encoded': bytes_feature(encoded_jpeg),
        'image/format': bytes_feature('jpeg'.encode()),
        'image/object/bbox/xmin': float_feature(xmin),
        'image/object/bbox/xmax': float_feature(xmax),
        'image/object/bbox/ymin': float_feature(ymin),
        'image/object/bbox/ymax': float_feature(ymax),
        'image/object/class/text': bytes_feature(class_name.encode()),
        'image/object/class/label': int64_feature(class_index),
        'image/object/difficult': int64_feature(difficult_obj),
        'image/object/truncated': int64_feature(truncated),
        'image/object/view': bytes_feature(poses.encode()),
    }))

def int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def float_feature(value):
    return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))

def create_record(directory):
    writer = tf.python_io.TFRecordWriter('out.record')
    subdirs = [name for name in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, name))]
    with open('label_map.pbtxt', 'w') as label_map_file:
        for idx, subdir in enumerate(subdirs):
            label_map_file.write('item {{\n  id: {0}\n  name: \"{1}\"\n  display_name: \"{1}\"\n}}\n\n'.format(idx+1, subdir))
            #class_dir = os.path.join(directory, subdir)
            #for f in os.listdir(class_dir):
            #    if f.endswith('jpg'):
            #        example = create_example(directory, subdir, idx+1, f)
            #        writer.write(example.SerializeToString())
    writer.close()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description = 'generate targets')
    parser.add_argument('-i', '--image-dir', type=str, help='The directory images are stored in')
    args = parser.parse_args()
    create_record(args.image_dir)
