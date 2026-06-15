import re
from collections import Counter
# CLARK COMPILER by kenneytube
# version 1.5 12th june

def clarkcompiler():
    print("\n+-------------------------------------------------+\n|                  CLARK COMPILER                 |\n+-------------------------------------------------+")
    main=input("\n1 - Item Count\n2 - Dupe Check\n3 - Owner Count\n4 - Deal Check\n\nSelection: ")
    if main=="1": itemcount()
    elif main=="2": dupecheck()
    elif main=="3": ownercount()
    elif main=="4": dealcheck()
    else: print("Invalid input.")
    clarkcompiler()

def dupecheck():
    print("\n===== DUPE CHECK =====")
    print("Paste your data below.")
    print("When finished, type END on a new line and press Enter.\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    content = "\n".join(lines)
    pattern = r'\[\\"(\d+_\d+\.\d+)\\",\\"([^"]+)\\"'
    matches = re.findall(pattern, content)
    ids = [item_id for item_id, _ in matches]
    counts = Counter(ids)

    id_to_name = {}
    for item_id, item_name in matches:
        id_to_name[item_id] = item_name
    duplicates = {item_id: count for item_id, count in counts.items() if count > 1}

    print("\n===== DUPE RESULTS =====")
    print(f"Total IDs found: {len(ids)}")
    print(f"Unique IDs: {len(counts)}")

    if duplicates:
        print("\nDuplicate IDs found:")
        for item_id, count in sorted(duplicates.items()):
            print(f"{item_id} ({count} times) - {id_to_name[item_id]}")
    else:
        print("\nNo duplicate IDs found.")

def itemcount():
    print("\n===== ITEM COUNTER =====")
    print("Paste your data below.")
    print("When finished, type END on a new line and press Enter.\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    content = "\n".join(lines)
    pattern = r'\[\\"(\d+_\d+\.\d+)\\",\\"([^"]+)\\"'
    matches = re.findall(pattern, content)
    item_names = [item_name for _, item_name in matches]
    counts = Counter(item_names)

    print("\n===== ITEM NAME COUNTS =====")
    print(f"Total items found: {len(item_names)}")
    print(f"Unique item names: {len(counts)}\n")

    for name, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print(f"{name}: {count}")
    print ("\n")

def ownercount():
    print("\n===== OWNER COUNTER =====")
    print("Paste your data below.")
    print("When finished, type END on a new line and press Enter.\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
        content = "\n".join(lines)
        pattern = r'\[\\"(\d+)_\d+\.\d+\\",\\"([^"]+)\\"'
        matches = re.findall(pattern, content)
        owner_ids = [owner_id for owner_id, _ in matches]
        counts = Counter(owner_ids)

    print("\n===== OWNER ID COUNTS =====")
    print(f"Total items found: {len(owner_ids)}")
    print(f"Unique owner IDs: {len(counts)}\n")

    for owner_id, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print(f"{owner_id}: {count}")
    print ("\n")

def dealcheck():
    print("\n===== DEAL CHECK =====")
    print("Paste your data below.")
    print("When finished, type END on a new line and press Enter.\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    content = "\n".join(lines)
    pattern = r'\\"(\d+_\d+\.\d+)\\"\s*,\s*\\"([^"]+)\\"'
    matches = re.findall(pattern, content)

    if not matches:
        print("No items found.")
        exit()
        
    owner_counts = Counter()

    for item_id, _ in matches:
        owner_id = item_id.split("_")[0]
        owner_counts[owner_id] += 1

    duplicate_owners = {
        owner_id: count
        for owner_id, count in owner_counts.items()
        if count > 1
    }

    print("\n===== DUPLICATE OWNER IDS =====")

    if not duplicate_owners:
        print("No duplicate owner IDs found.")
    else:
        for owner_id, count in sorted(duplicate_owners.items()):
            print(f"\nOwner ID: {owner_id} ({count} items)")
            items = []
            for item_id, item_name in matches:
                if item_id.startswith(owner_id + "_"):
                    unique_id = int(item_id.split(".")[-1])
                    items.append((unique_id, item_name, item_id))

            items.sort(key=lambda x: x[0])
            for unique_id, item_name, item_id in items:
                print(f"   {item_name} | {item_id}")

clarkcompiler()