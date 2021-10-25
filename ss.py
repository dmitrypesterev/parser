import json


# thatpath = "https://hola-korean-assets.s3.us-east-2.amazonaws.com/vocabulary/"
# file = open('selectedemojies.json', encoding='utf-8')
# allemojies = json.load(file)

# # for emoji in emojies:
# #     newemojies.append({
# #         "id": emoji["img"].split('/')[-1][0:-4],
# # 		"name": emoji["name"],
# #         "translate": emoji["name"],
# # 		"img": emoji["img"],
# #         "group": ""
# #     })

# newemojies = []

# for emoji in allemojies:
#     newpath = thatpath + emoji["img"].split('/')[-1]
#     newemojies.append({
#         "id": emoji["id"],
# 		"name": emoji["name"],
#         "translate": emoji["translate"],
# 		"img": newpath,
#         "group": emoji["group"]
#     })

file = open('allemojies.json')
allemojies = json.load(file)
newemojies = []

for emoji in allemojies:
    newemojies.append({
        "id": emoji["id"],
		"name": emoji["name"],
        "translate": emoji["translate"],
		"img": emoji["img"],
        "group": ""
    })



with open('allemojies.json', 'w', encoding='utf-8') as json_file:
    json.dump(newemojies, json_file, indent=4, sort_keys=True, ensure_ascii=False)

