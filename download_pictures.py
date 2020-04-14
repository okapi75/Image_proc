#!/usr/bin/env python
# coding: utf-8
import requests
import argparse
# from tqdm import tqdm

def download_ims_from_list(list_of_ims,save_path):
    for i,url in enumerate(list_of_ims):
        try:
            img_data = requests.get(url).content
            with open(save_path+"_"+str(i)+".jpg", 'wb') as f:
                f.write(img_data)
        except Exception as e:
            print("download error with url"+str(i))
        
parser = argparse.ArgumentParser(description='Download images from url list with multithreading')
parser.add_argument('url_list', type=str, help='tsv list of urls to images')
parser.add_argument('n_threads', type=int, help='number of processes')
parser.add_argument('cur_thread', type=int, help='the id of current process')

if __name__=="__main__":
    args = parser.parse_args()
    with open(args.url_list) as f:
        data = f.readlines()
        if not "http" in data[0]:
            data = data[1:]
            
    N = len(data)
    i_start = args.cur_thread * N // args.n_threads
    i_fin = (args.cur_thread + 1) * N // args.n_threads
    data = data[i_start:i_fin]
    save_path = "./downloaded_images/" + str(args.cur_thread)
    download_ims_from_list(data,save_path)




