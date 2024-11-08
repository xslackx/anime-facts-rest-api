import json
import random
from html import unescape

with open('./db/animedb.json', 'r') as stored:
    db = json.loads(stored.read())
    
''''
Get all facts related to an Anime:
{
	success:true,
	total_facts: 8,
	anime_img:"https://eaxmpleimage.com/",
	data: [
		{
			fact_id: 1,
			fact: "Ishvalans And Ametris Conflict Is Based On Hokkaido s Ainu People"
		},
		{
			fact_id: 2,
			fact: "Arakawa Actually Bought Military Prop Guns For Drawing References"
		},
		...
	]
}
'''
def v1_get_facts(req: list, res):

    def get_facts(anime):
        if anime["name"] == req:
            return {"facts": anime["facts"]}
        else: return
          
    fact = list(map(get_facts, db["anime_facts_api"]["animes"]) )   
    msg = list(filter(lambda item: item is not None, fact))
    
    total_facts = len(msg[0]['facts'])
    data_facts = []

    for index, anime_fact in enumerate(msg[0]["facts"]):
        data_facts.append({"fact_id": index, "fact": anime_fact})

    response: dict
    
    if any(msg):
        url: str = ""
        for img in db["anime_facts_api"]["media"]:
            if img['anime_name'] == req:
                url = img['anime_img']
            
        response = {"success": True, "total_facts": total_facts ,
                    "anime_img":url,"data": data_facts}
    else:
        response = {"success": False,"total_facts": False,
                    "anime_img":url, "data": []}  
        
    res.write(json.dumps(response).encode())


''''
Get all facts related to an Anime
{
	success:true,
	data: {
			fact_id: 2,
			fact: "Arakawa Actually Bought Military Prop Guns For Drawing References"
	}
	
}
'''
def v1_get_facts_by_id(req, res):
    
    def get_by_id(anime):
        if anime["name"] == req[0]:
            if req[1] <= len(anime["facts"])-1:
                return anime["facts"][req[1]]
            else:
                if req[1] > len(anime["facts"]):
                    return anime["facts"][-1]
                 
    fact = list(map(get_by_id, db["anime_facts_api"]["animes"]))
    msg = list(filter(lambda item: item is not None, fact))
    
    
    
    if len(msg) > 0:
        res.write(json.dumps({ "success":True,
                              "data": 
                                  { 
                                  "fact_id": req[1],
                                  "fact": unescape(msg[0])
                                  }
                              }).encode())
    else:
        res.write(json.dumps({ "success":False, "data": {} }).encode())
        
        
'''''
Get all the available anime's list:

{
	success:true,
	data: [
		{
			anime_id: 1,
			anime_name: "bleach",
			anime_img: "https://eaxmpleimage.com/"
		},
		{
			anime_id: 2,
			anime_name: "black_clover",
			anime_img: "https://eaxmpleimage2.com/"
		},
		...
	]
}
'''''    
def v1_get_animes(req, res):
    
    if req != 'all': return
    
    def get_animes(media, animes):
        return {"anime_name":animes["name"], "anime_img": media["anime_img"]}

    msg = list(map(get_animes, db["anime_facts_api"]["media"], db["anime_facts_api"]["animes"]))
    
    response: dict
    
    if any(msg):
        response = {"success": True, "data": msg}
    else:
        response = {"success": False, "data": []}  
        
    res.write(json.dumps(response).encode())

