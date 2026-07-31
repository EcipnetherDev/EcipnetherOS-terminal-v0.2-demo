#import hashlib
from pathlib import Path
#import os

#for dirs in os.walk("."):
    #print (dirs)

#for file in dirs:
    #print(" ", file)

yol = Path(".")

print(yol.exists())
print(yol.is_dir())