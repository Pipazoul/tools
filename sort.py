import os
import sys    
path = sys.argv[1]
results = []
data_paths = [os.path.join(pth, f)
    for pth, dirs, files in os.walk(path) for f in files]


print(sys.argv)
query = sys.argv[2]
for file in data_paths :
    print(file)
    with open(file) as text :
        line = text.read()
        for part in line.split():
            if query in part:
                print(part)
                results.append(part)
                with open(query+'.txt', "a") as textOutput:
                    textOutput.write(part + "\n")

for result in results :
    print(result)
        
        
