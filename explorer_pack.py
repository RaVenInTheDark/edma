import csv
import os
jumps = 0

def startjump(event):
    if event["JumpType"] == "Supercruise":
        return "Entering Supercruise"
        
    if event["JumpType"] == "Hyperspace" and jumps <= 1:
        return event["StarSystem"]


def fsdtarget(event):
    global jumps
    if event["StarClass"] in list("OBAFGKM"):
        scoop = "Star is scoopable"
    else:
        scoop = "Star not scoopable"
        
    jumps = event['RemainingJumpsInRoute'] if 'RemainingJumpsInRoute' in event.keys() else 0

    return f"Next jump: {event['Name']} | {scoop} | {str(event['RemainingJumpsInRoute'])  + ' Jump(s) left' if 'RemainingJumpsInRoute' in event.keys() else 'Last jump'}"


def supercruiseexit(event):
    return f"Exited supercruise in {event['StarSystem']} near {event['Body']}"



events = [startjump, fsdtarget, supercruiseexit]