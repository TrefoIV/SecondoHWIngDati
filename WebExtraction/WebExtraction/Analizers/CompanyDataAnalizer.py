from json import JSONDecoder
import os.path as pathLib
import sys
from time import sleep

decoder = JSONDecoder()
valueCompanies, marketCompanies = None, []

path = pathLib.dirname(pathLib.relpath( "__file__"))
vComPath = path.join("../../valueCompanies.json")
markComPath = path.join("../../companiesMarketCap.json")

with open(vComPath, "r", encoding="utf-8" ) as valueF:
    with open(markComPath, "r", encoding="utf-8" ) as marketCapF:
        valueCompanies = valueF.read()
        valueCompanies = decoder.decode(valueCompanies)

        for index, line in enumerate(marketCapF):
            if line == "[\n" or line == "]":
                continue
            if line[-2] == ",":
                line = line[:len(line) - 2]
            comp = decoder.decode(line)
            marketCompanies.append(comp)

def compute_percentage(name_in : str, name_out : str):
    len_in = len(name_in)
    last_index_out = len(name_out) -1
    start_index = name_out.find(name_in)
    end_index = start_index + len_in - 1
    validate = True

    check = lambda char : char <= 'Z' and char >= 'A'

    if start_index != 0:
        if check(name_out[start_index - 1]):
            validate = False
    if end_index != last_index_out:
        if check(name_out[end_index + 1]):
            validate = False
    if validate:
        return (len(name_in) / len(name_out) ) * 100
    else:
        return 0


def compute_name_similarity(name, name_1):
    res = {"perc" : 0}
    if name in name_1 or name_1 in name:
        if name in name_1:
            perc = compute_percentage(name, name_1)
        else:
            perc = compute_percentage(name_1, name)
        res = {
            "valueName" : name_1,
            "marketName" : name,
            "perc" : perc
            }
    return res


exactMatch = []

non_exact_match = []

for company in marketCompanies:
    name = company["name"].upper().replace("\n", "").replace("-", " ")
    maxPerc = {"perc" : 0}
    foundExact = False
    for company_1 in valueCompanies:
        name_1 = company_1["name"].upper().replace("\n", "").replace("-", " ")
        if name == name_1:
            exactMatch.append({
                "valueName" : company_1["name"],
                "marketName" : company["name"]
            })
            foundExact = True
            break
        else:
            temp = compute_name_similarity(name, name_1)
            if temp["perc"] > maxPerc["perc"]:
                maxPerc = temp

           
    if not foundExact and maxPerc["perc"] != 0:
        non_exact_match.append(maxPerc)
    



print(f"len {len(exactMatch)}")
print("=================================")
print(f"len non exact {len(non_exact_match)}")
for i in range(50):
    if i < len(non_exact_match):
        print(non_exact_match[i])

