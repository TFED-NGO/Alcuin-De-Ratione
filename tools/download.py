import time
import requests

START_INDEX = 1
MAX_IMAGES = 307

def main():
    for i in range(START_INDEX, MAX_IMAGES):
        download_img(i)

def url(num: int):
    page_index_in_hex = hex(num)[2:].zfill(6)
    return f'https://dlcs.bl.digirati.io/iiif-img/v3/2/3/81055___vdc_100059910362.0x{page_index_in_hex}/full/1743,2048/0/default.jpg'

def download_img(num: int):
    data = requests.get(url(num)).content 
    f = open(f'download/img{num}.jpg','wb') 
    f.write(data) 
    f.close()

if __name__ == "__main__":
    main()