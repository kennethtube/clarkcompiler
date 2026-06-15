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

def main(): #command center
    req=input(">>> ")
    if req=="item":itemcount()
    elif req=="allowner":allowners()
    elif req=="owner":ownersearch()
    elif req=="dupe":dupecheck()
    elif req=="raw":raw()
    elif req=="help":helppage()
    else:
        print("Invalid input.")
        main()

def helppage(): #help page
    print("===== HELP PAGE =====")
    print("Commands")
    print("> item\n    └ Identifies the names of items within the targets inventory and the amount of times they appear.\n    └ [ITEM_ID]: [# POSSESSED]")
    print("> allowner\n    └ Identifies all owners of items within the targets inventory and the amount of times they appear.\n    └ [USER_ID]: [# POSSESSED]")
    print("> dupe\n    └ Identifies repeat item owner USERID within a targets inventory, the name of the item, and the amount of times they appear.\n    └ [ITEM_ID] (ITEM_NAME): [# POSSESSED]")
    print("> raw\n    └ Allows you to re-input the rawdata to compile from.\n")
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

def itemcount():
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

def dupecheck():
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
    print(f"Total IDs found: {len(ids)}")
    print(f"Unique IDs: {len(counts)}")

    if duplicates:
        for item_id, count in sorted(duplicates.items()):
            print(f"> {item_id} ({id_to_name[item_id]}): {count}")
    else:
        print("\nNo duplicate IDs found.")
    print("\n")
    main()

initialize()
print("Error 100")