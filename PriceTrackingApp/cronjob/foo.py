import os.path
import datetime

f = open(os.path.abspath("test_file.txt"), 'a')

f.write(f"\nhi. task ran at {datetime.datetime.now()}")

# input("waiting for you...")