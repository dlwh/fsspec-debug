import fsspec


total = 0

for f in fsspec.open_files('libarchive://data/*.txt::data.tgz', 'r'): 
   total += len(f.open().read())

# if you fix the exception (and don't mess anything else up) you should get this value
assert total == 30066235
