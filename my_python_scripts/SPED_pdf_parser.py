import sys
import re

file_path = sys.argv[1]
regex = r'^SAU #(\d+)\s*(.*)\s*([^,\n]+)[^:]*:\s*(.*)[^:]*:\s*[^:]*:\s*(.*)'

csvHeader = 'Sau ID,SAU Name, SAU SpEd Director Name, SAU SpEd Director Email, Phone\n'

with open(file_path, 'r') as file:
    matches = re.findall(regex, file.read(), re.MULTILINE)
    #print(matches)
    with open('SAU.csv', 'w') as csv:
        csv.write(csvHeader)
        for m in matches:
            #print(m)
            tmp = '"'+(m[1]+" SAU Office")+'"'
            s=f'{m[0]},{tmp},{m[2]},{m[4]},{m[3]}\n'
            csv.write(s)
            print(s)
