import tempfile

commandname = "cat"

f = tempfile.NamedTemporaryFile(delete=False)
f.write(b'oh hello there')
f.close() # file is not immediately deleted because we
          # used delete=False
import subprocess
res = subprocess.call(["wc", f.name])
print (res)

#https://stackoverflow.com/questions/15169101/how-to-create-a-temporary-file-that-can-be-read-by-a-subprocess

