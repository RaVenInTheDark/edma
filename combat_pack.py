def bounty(event):
    rewards = []

    for reward in event["Rewards"]:
        rewards.append(f"{reward['Reward']} credits from {reward['Faction']}")
        
    text = f"Destroyed ship {event['Target']} from faction {event['VictimFaction']}. Rewards: {'newline'.join(rewards)}"

    return text.replace("newline", "\n") #workaround to deal with fstring issues


def shiptargeted(event):
    if not event["TargetLocked"]:
        return None
    
    if not "Ship_Localised" in event.keys():
        event["Ship_Localised"] = event["Ship"]

    if event["ScanStage"] == 0:
        return f"Scanning {event['Ship_Localised']}"
    
    if event["ScanStage"] == 1:
        return f"Scanning {event['Ship_Localised']}\n{event['PilotName_Localised']}\n{event['PilotRank']}"

    if event["ScanStage"] == 2:
        return f"Scanning {event['Ship_Localised']}\n{event['PilotName_Localised']}\n{event['PilotRank']}\nShields: {event['ShieldHealth']}\nHull: {event['HullHealth']}"

    if event["ScanStage"] == 3 and "Bounty" not in event.keys():
        return f"Scanning {event['Ship_Localised']}\n{event['PilotName_Localised']}\n{event['PilotRank']}\nShields: {event['ShieldHealth']}\nHull: {event['HullHealth']}\n{event['Faction']}\n{event['LegalStatus']}"

    else:
        return f"Scanning {event['Ship_Localised']}\n{event['PilotName_Localised']}\n{event['PilotRank']}\nShields: {event['ShieldHealth']}\nHull: {event['HullHealth']}\n{event['Faction']}\n{event['LegalStatus']}\nEstimated Bounty: {event['Bounty']}"



def shieldstate(event):
    if event['ShieldsUp']:
        return "Shields online"
    else:
        return "Shields offline"



def heatdamage(event):
    return "Taking heat damage!"



def heatwarning(event):
    return "Warning: Critical Temperature!"


events = [bounty, shieldstate, shiptargeted, heatdamage, heatwarning]