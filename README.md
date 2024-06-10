# merrer
M(app)er (and) R(educ)er

[G4G](https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/) with comments removed, utf tag added, and converted to Python3. 

Works over text files with a Python3 installed and execute permissions.

```
mapred streaming \
  -input /user/sandbox/books \
  -output /user/sandbox/words \
  -mapper mapper.py \
  -reducer reducer.py \
  -file scripts/mapper.py \
  -file scripts/reducer.py
```

Used datasets

https://raw.githubusercontent.com/cd-public/books/main/pg1342.txt  
https://raw.githubusercontent.com/cd-public/books/main/pg84.txt  
https://raw.githubusercontent.com/cd-public/books/main/pg768.txt  



