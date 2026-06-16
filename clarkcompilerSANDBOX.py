import re
from collections import Counter
# CLARK COMPILER by kenneth

def initialize():
    print("\n+-------------------------------------------------+\n|                  CLARK COMPILER                 |\n+-------------------------------------------------+")
    raw()

def raw():
    global rData
    print("\n> Please input your raw data")
    rData=input(">>> ")
    rData=str(rData)
    print("\n> Raw data saved")
    main()

def main():
    req=input(">>> ")
    req=req.lower()
    if req=="item":print("blub")
###
    elif req=="showraw":
        print(rData)
        main()
    elif req.startswith("searchowner "):
        ownerID = req.split(" ", 1)[1]
        searchOwner(ownerID)
###
    elif req=="raw":raw()
    else:
        print("Invalid input.")
        main()

def searchOwner(ownerID): #search by ownerID
    global rData
    content = rData
    pattern = r'\[\\"(\d+_\d+\.\d+)\\",\\"([^"]+)\\"'
    matches = re.findall(pattern, content)
    owner_items = [
        (item_id, item_name)
        for item_id, item_name in matches
        if item_id.split("_")[0] == ownerID]

    item_names = [item_name for _, item_name in owner_items]
    counts = Counter(item_names)

    print(f"\n===== RESULTS FOR {ownerID} =====")
    print(f"Total items found: {len(item_names)}")
    print(f"Unique item names: {len(counts)}\n")

    if not owner_items:
        print("No items found.")
        return

    for item_id, item_name in owner_items:
        print(f"> {item_id} ({item_name})")
    main()

initialize()