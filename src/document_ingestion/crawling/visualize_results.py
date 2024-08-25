import os
import json

def analyze_content_structure(data, output_dir="data/formatted/"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Number of URLs parsed
    num_urls = len(data)

    # Sample files
    sample_markdown = []
    sample_content = []

    for item in data[:3]:  # Limiting to first 3 items for samples
        sample_markdown.append(f"# {item['metadata']['sourceURL']}\n{item['markdown']}")
        sample_content.append(f"# {item['metadata']['sourceURL']}\n{item['content']}")

    # Writing summary stats
    with open(os.path.join(output_dir, 'summary.txt'), 'w', encoding='utf-8') as f:
        f.write(f"Number of URLs parsed: {num_urls}\n")

    # Writing sample markdown file
    with open(os.path.join(output_dir, 'sample_markdown.md'), 'w', encoding='utf-8') as f:
        f.write("\n\n".join(sample_markdown))

    # Writing sample content file
    with open(os.path.join(output_dir, 'sample_content.md'), 'w', encoding='utf-8') as f:
        f.write("\n\n".join(sample_content))

    print(f"Summary and samples written to: {output_dir}")

# Print current working directory for debugging
print(f"Current working directory: {os.getcwd()}")

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the data file relative to the script's location
data_file_path = os.path.join(current_dir, 'data', 'raw', 'supabase.com_docs_.json')

# Print the path we're trying to open for debugging
print(f"Attempting to open file at: {data_file_path}")

# Check if the file exists before trying to open it
if not os.path.exists(data_file_path):
    print(f"File does not exist at: {data_file_path}")
    exit(1)

# Load your data from the file
with open(data_file_path, 'r') as f:
    data = json.load(f)['data']  # Assuming 'data' is nested under a key in your JSON

# Analyze content structure
analyze_content_structure(data)

# Print summary stats
print(f"Number of URLs parsed: {len(data)}")