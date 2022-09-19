import os
os.makedirs("save_test", exist_ok=True)

with open('./save_test/test.txt', 'a') as file:
    file.write('whatever ')
    
with open('./save_test/test.txt', 'r') as file:
    x = file.readlines()
    print(x[0])