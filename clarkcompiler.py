import re
from collections import Counter
# CLARK COMPILER by kenneth

def initialize(): #main open
    print("\n+-------------------------------------------------+\n|                  CLARK COMPILER                 |\n+-------------------------------------------------+")
    raw()

def raw(): #rawdata input
    global rData
    print("\n> Please input your raw data")
    rData=input(">>> ")
    rData=str(rData)
    print("\n> Raw data saved")
    main()

def main(): #command center#########################
    req=input(">>> ")
    req=req.lower()
    if req=="items":itemcount()
    elif req=="allowners":allowners()
    elif req=="dupes":dupecheck()
    elif req=="raw":raw()
    elif req=="help":helppage()
    elif req=="showraw":
        print(rData)
        print("\n")
        main()
    elif req.startswith("searchowners "):
        ownerID = req.split(" ", 1)[1]
        searchOwner(ownerID)
    elif req.startswith("searchitems "):
        itemName = req.split(" ", 1)[1]
        searchitem(itemName)
    else:
        print("Invalid input.")
        main()

def helppage(): #help page
    print("===== HELP PAGE =====")
    print("Commands")
    print("> allowners\n    └ Identifies all owners of items within the targets inventory and the amount of times they appear.\n    └ [USER_ID]: [# POSSESSED]")
    print("> dupes\n    └ Identifies repeat item owner USERID within a targets inventory, the name of the item, and the amount of times they appear.\n    └ [ITEM_ID] (ITEM_NAME): [# POSSESSED]")
    print("> items\n    └ Identifies the names of items within the targets inventory and the amount of times they appear.\n    └ [ITEM_ID]: [# POSSESSED]")
    print("> raw\n    └ Allows you to re-input the rawdata to compile from.\n")
    print("> searchitems ONLYTWENTYCHARACTERS\n    └ Identifies items with matching item names to the requested item (ignores capitalization).\n    └ [ITEM_ID] ([ITEMNAME])")
    print("> searchowners 1234567890\n    └ Identifies items with matching ownerIDs to the requested item.\n    └ [ITEM_ID] ([ITEMNAME])")
    print("> showraw\n    └ Allows you to view the rawdata which is being compiled from.\n")
    main()

def allowners(): #reveals owners
    global rData
    content = rData
    pattern = r'\[\\"(\d+)_\d+\.\d+\\",\\"([^"]+)\\"'
    matches = re.findall(pattern, content)
    owner_ids = [owner_id for owner_id, _ in matches]
    counts = Counter(owner_ids)

    print("\n===== OWNERID RESULTS =====")
    print(f"Total items found: {len(owner_ids)}")
    print(f"Unique owner IDs: {len(counts)}\n")

    for owner_id, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print(f"> {owner_id}: {count}")
    print("\n")
    main()

def itemcount(): #shows all items 
    global rData
    content = rData
    pattern = r'\[\\"(\d+_\d+\.\d+)\\",\\"([^"]+)\\"'
    matches = re.findall(pattern, content)

    item_names = [item_name for _, item_name in matches]
    counts = Counter(item_names)

    print("\n===== ITEM NAME COUNTS =====")
    print(f"Total items found: {len(item_names)}")
    print(f"Unique item names: {len(counts)}\n")

    for name, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print(f"> {name}: {count}")

    print()
    main()

def dupecheck(): #checks for duplicate itemIDs
    global rData
    content = rData
    pattern = r'\[\\"(\d+_\d+\.\d+)\\",\\"([^"]+)\\"'
    matches = re.findall(pattern, content)
    ids = [item_id for item_id, _ in matches]
    counts = Counter(ids)

    id_to_name = {}
    for item_id, item_name in matches:
        id_to_name[item_id] = item_name

    duplicates = {
        item_id: count
        for item_id, count in counts.items()
        if count > 1}

    print("\n===== DUPE RESULTS =====")
    print(f"Total Item IDs found: {len(ids)}")
    print(f"Unique Item IDs: {len(counts)}\n")

    if duplicates:
        for item_id, count in sorted(duplicates.items()):
            print(f"> {item_id} ({id_to_name[item_id]}): {count}")
    else:
        print("\nNo duplicate IDs found.")
    print("\n")
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
    print("\n")
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
    owner_items.sort(key=lambda x: int(x[0].split(".")[-1]))
    item_names = [item_name for _, item_name in owner_items]
    counts = Counter(item_names)

    print(f"\n===== RESULTS FOR {ownerID} =====")
    print(f"Total items found: {len(item_names)}")
    print(f"Unique item names: {len(counts)}\n")

    if not owner_items:
        print("No items found.")

    for item_id, item_name in owner_items:
        print(f"> {item_id} ({item_name})")
    print("\n")
    main()

initialize()
print("Error 100")