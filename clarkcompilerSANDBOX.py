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
    elif req.startswith("searchitem "):
        itemName = req.split(" ", 1)[1]
        searchitem(itemName)
###
    elif req=="raw":raw()
    else:
        print("Invalid input.")
        main()

def searchitem(itemName): #search by itemName
    global rData
    itemTitle=itemName.upper()
    content = rData
    pattern = r'\[\\"(\d+_\d+\.\d+)\\",\\"([^"]+)\\"'
    matches = re.findall(pattern, content)
    found_items = [
        (item_id, name)
        for item_id, name in matches
        if name.lower() == itemName.lower()
    ]

    def sort_key(item):
        item_id = item[0]
        unique_part = item_id.split(".")[-1]
        return int(unique_part)

    found_items.sort(key=sort_key)

    print(f"\n===== RESULTS FOR {itemTitle} =====")
    print(f"Total items found: {len(found_items)}\n")

    if not found_items:
        print("No items found.")

    for item_id, name in found_items:
        print(f"> {item_id} ({name})")
    main()

initialize()