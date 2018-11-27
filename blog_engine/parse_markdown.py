"""
Step 1 - Scans the content folder for '.md' and '.markdown' files

Step 2 - Check 'blog/'filename'.html' for already processed files.

Step 3a - If 2 == False, Parse Markdown and Save as blog/filename.html
Step 3b - If 2 == True, Skip and go to the next file
"""

from markdown import markdown
from pathlib import Path
import json

content_libraries = ['podcasts', 'microblog']

def render_post(md_content):
    with open(md_content):
        post = md_content.split('\n\n', 2)
        metadata_string = post[0]
    
    metadata = {}

    for line in metadata_string.split('\n'): 
        line_data = line.split(': ',2 )
        metadata[line_data[0].lower()] = line_data[1]

    metadata['content'] = markdown(post[-1])
    return metadata     
    

def check_for_json_file(json_file):
    if not Path(json_file).exists():
        with open(json_file) as f:
            return f.write('')


def add_json_content(json_object, metadata):
    return json_objects['items'].append(metadata)
    
    
    