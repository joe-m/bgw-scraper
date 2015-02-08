# -*- coding: utf-8 -*-
"""
Created on Mon Feb 02 17:36:16 2015

@author: Joseph

TODO: 
-write new bit that isolates displacement if included, then analyze
-figure out what's going on with the low number in class_dict
"""

import praw
#import matplotlib

def start_praw():
    r = praw.Reddit("Scraper for /r/bikesgonewild V0.1 by /u/...")
    #useragent string
    return r

def get_sub_data(url, r):    
    sub = r.get_content(url, limit = None)    # generator object
    cont = [str(x) for x in sub]
    print "total posts:", len(cont)
    return cont

def categorize(sub_cont):
    brand_ids = {"yams" : ["yamaha", "fz", "vstar" , "tenere", "wt"],
                 "suzis" : ["suzuki", "zuki", "gsx", "gixxer", "sv", "busa", 
                                "hayabusa"],
                 "dukes" : ["ducati", "monster", "diavel", "panigale"],
                 "hondas" : ["honda", "cb", "cbr", "crf", "gold wing"],
                 "harleys" : ["fatboy", "harley", "davidson"],
                 "kawas" : ["kawasaki", "kawa", "ninja", "klr"],
                 "other" : ["ktm", "bmw", "guzzi", "triumph", "striple", 
                                "aprilia"]}
    class_dict = dict(yams = 0, hondas = 0, suzis = 0,
                     dukes = 0, harleys = 0, kawas = 0, other = 0)
                     #will count posts in these value-ints of brands
                     
    for post in sub_cont:     #iter thru posts in BGW
        for i in brand_ids.keys():  #iter thru brands of interest
            for term in brand_ids.get(i):   #iter thru terms in brandlist
                if term in post:            #if brand term in post
                    class_dict[i] = class_dict.get(i) + 1 #count
    
    return class_dict

                
def main():
    r = start_praw()
    sub_cont = get_sub_data("http://www.reddit.com/r/bikesgonewild", r)    
    cat_result = categorize(sub_cont)
    return cat_result
    
    
    
    
    
    
    
    
    
    