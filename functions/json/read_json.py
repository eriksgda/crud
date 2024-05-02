import json

def readJson(file_name):
  try:
    with open(file_name + '.json', 'r') as file:
      data = json.load(file)
      file.close()
    return data
  except FileNotFoundError:
    return []