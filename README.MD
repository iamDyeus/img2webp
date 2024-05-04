# IMG 2 WEBP
IMG2WEBP is a Python-based script/application for converting and optimizing images in bulk initially made for web development optimization.

## Inspiration 
Saw a Lighthouse report from Cloudflare indicating that my site was loading too slowly due to the images. Conventionally, I would have had to compress each image individually and then convert them to WEBP format. However, instead of doing this manually, I came up with the idea of creating a Python script that can handle this process in bulk for me.

## Results
After using this, my images folder size decreased significantly, from 105MB to just 9MB!


## Installation
locally clone/download this repo, `cd` to the project folder and then follow these steps : 

1. Make Virtual Environment :
`python -m venv .env`

2. Acivate ENV :
`.env\scripts\activate`

3. Install requirements : 
`pip install -r requirements.txt`

4. go to source code directory : 
`cd src`

5. Run `main.py` : 
`python main.py`
