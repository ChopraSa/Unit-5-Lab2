
with open("sample.ini") as file:
        data = file.read()

def variables(data):
     for line in data.split('\n'):
        print(line)
        
        line2= line.split("=")
        print(line2[0])
       
    
variables(data)
