import json
import csv
import sys
import os

x=10
y = [1,2,3,4,5]

def convert_csv_to_json(input_file,output_file):
    """Convert a CSV file to JSON format."""
    result = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.append(dict(row))
    return result

def filter_by_field(data,field,value):
    """Filter list of dicts by a field value."""
    filtered=[]
    for item in data:
        if item.get(field)==value:
            filtered.append(item)
    return filtered

def summarize(data, field):
    """Count unique values in a field."""
    counts = {}
    for item in data:
        val = item.get(field, 'unknown')
        if val in counts:
            counts[val]+=1
        else:
            counts[val] = 1
    return counts

def save_json(data, path):
    """Save data as JSON file."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f'Saved {len(data)} records to {path}')

def print_summary(summary):
    """Print summary dictionary."""
    print('Summary:')
    for k,v in summary.items():
        print(f'  {k}: {v}')

def main():
    if len(sys.argv)<3:
        print('Usage: python script.py input.csv output.json')
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    if not os.path.exists(input_path):
        print(f'File not found: {input_path}')
        sys.exit(1)
    data = convert_csv_to_json(input_path, output_path)
    summary = summarize(data, 'category')
    print_summary(summary)
    save_json(data, output_path)
if __name__ == '__main__':
    main()
