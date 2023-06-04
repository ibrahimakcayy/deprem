import requests
import json


try:
    r = requests.get('http://www.koeri.boun.edu.tr/scripts/lasteq.asp')

    a= r.text.split('<pre>')[1].split("</pre>")[0].split("\r\n")[7::]

    z=""

    for i in range(len(a)-2):
        
        a[i]=a[i].split()
        b=["",""]
        c=""
        d=""
        
        if a[i][-1] != "Quick":
            for l in a[i][-3::]:
                c=c+l
                
            b[1]=c
            for k in a[i][8:-3]:
                d=d+k
                
            b[0]=d
            
        else:
            for m in a[i][8:-1]:
                c=c+m

            b[1]=a[i][-1]
            b[0]=c

        x = {
            "id": i+1,
            "date": a[i][0],
            "timestamp": a[i][1],
            "latitude": float(a[i][2]),
            "longitude": float(a[i][3]),
            "depth": float(a[i][4]),
            "size": {
                "md": float(a[i][5].replace('-.-', '0')),
                "ml": float(a[i][6].replace('-.-', '0')),
                "mw": float(a[i][7].replace('-.-', '0')),
                },
            "location": b[0],
            "attribute":b[1]
        }

        y = json.dumps(x)
        z=z+","+y

    z="["+z[1::]+"]"
    
    f = open("demo.json", "w")
    f.write(z)
    f.close()
    print("done")
    
except Exception as e:
    print(e)
