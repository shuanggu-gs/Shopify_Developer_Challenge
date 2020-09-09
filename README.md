# Shopify-Developer-Challenge
It's a private repo for solving Shopify Developer Intern Challenges

The goal of this project is to build up an image repository and support to search an image by text or search similar images.

## demo

![](shopify_demo.gif)

## Setup

Make sure you have installed packages listed below

``pip install numpy``

``pip install pandas``

``pip install json``

``pip install requests``

``pip install Pillow``

``pip install imageio``

``pip install -U scikit-image``


## Structure

- [CBIR](https://github.com/pochih/CBIR) - Content-based Image Retrieval
    - cache
    - features files
    
- datasets
    - 10 classes
- image-repo
    - backend.py
    - frontend.css
    - frontend.js
    - frontend.html
- prepare
    - prepare [ImageNet](http://www.image-net.org/) urls
    

## Run

Git clone this project, open terminal and navigate to project directory


``cd image-repo``

`python3 backend.py`

open `http://localhost:9998/` and you could play it!



