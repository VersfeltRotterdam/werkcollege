import requests

def _sent_score(names, score, route):
    assert names != None, f"Please fillout your name(s)."
    
    assert score != None, f"Please send a score, no scoure was found"
    assert route != None, f"Please send a route, no route was found"
    
    url = "https://rotterdam.webhook.office.com/webhookb2/062092c2-082c-4d2b-9028-06a44c3f63c7@49c4cd82-8f65-4d6a-9a3b-0ecd07c0cf5b/IncomingWebhook/41cac3178ee14f27908b98b000ff61f7/6eb92335-9829-43be-9664-8e7e4642a2a2"
    myobj = {"text" : f"{names} : {score}, route = {route}"}
    x = requests.post(url, json = myobj)
    
    assert x.text == "1", f"Something went wrong with sending in your solution, please sent your scores via Teams to Pieter. Error message = {x.text}"