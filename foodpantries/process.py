import json
import re

file = open("output.json", "r+")

data = json.load(file)
formattedData = ""

text = str(data)
text = text.replace(r"\r", "").replace(r"\n", "").replace(r"\t", "").replace(r"', '", ",").replace('{"data": ["', '{"data": [').replace('"]},', ']},').replace("']}, {'data':", "]},{\"data\":").replace("['", "[").replace("']", "]").replace("]},{ [", "],[").replace("'data'", '"data"').replace('\\', '\\\\').replace('"free"', "'free'")
formattedData += text

newJson = json.loads(formattedData)
for element in newJson:
    if(len(element["data"]) > 3):
        element["data"].pop(0)
        element["data"].pop(0)
        element["data"].pop(0)

text = open("text.txt", "r+")

text.write(formattedData)
text.close()

with open("fO.json", "w") as outfile:
    json.dump(newJson, outfile)