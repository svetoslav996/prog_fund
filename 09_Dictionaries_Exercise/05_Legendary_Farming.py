legendary_item = ""
materials = {"motes": 0, "shards": 0, "fragments": 0}
junk = {}

while materials["motes"] < 250 and materials["fragments"] < 250 and materials["shards"] < 250:
    input_str = input().lower()
    input_tokens = input_str.split()

    for i in range(0, len(input_tokens), 2):
        quantity = int(input_tokens[i])
        material = input_tokens[i + 1]

        if material in ["shards", "fragments", "motes"]:
            materials[material] += quantity
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

        if materials["shards"] >= 250 or materials["fragments"] >= 250 or materials["motes"] >= 250:
            break

if materials["shards"] >= 250:
    legendary_item = "Shadowmourne"
    materials["shards"] -= 250
elif materials["fragments"] >= 250:
    legendary_item = "Valanyr"
    materials["fragments"] -= 250
else:
    legendary_item = "Dragonwrath"
    materials["motes"] -= 250

print(f"{legendary_item} obtained!")

for item, value in sorted(materials.items(), key=lambda x: (-x[1], x[0])):
    print(f"{item}: {value}")

for item, value in sorted(junk.items()):
    print(f"{item}: {value}")