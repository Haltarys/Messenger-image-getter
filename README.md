# Messenger-image-getter
Quick script to download all images of a Messenger conversation

# How to use

- Edit `index.py` with your Facebook credentials
- `pip install fbchat`
- Fix the library installed (more details in `requirements.txt`)
- run the Python script
- If it works, redirect the output to a file: `python3 index.py > data`
- Edit the file so that it only contains the URLs of the images: `tail -n +2 data > data`
- `mkdir images && cd images`
- `wget -i ../data`
- to rename all images with a number: `../script.sh`
