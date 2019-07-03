import hashlib
import sys

uhash=str(sys.argv[1])
cnt=999
while(cnt<10000):
    number=str(cnt)
    res=hashlib.md5(number.encode())
    fres=res.hexdigest()
    if fres==uhash:
        print("PIN >>",cnt)
        sys.exit()
    cnt=cnt+1
