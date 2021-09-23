import os

for data in os.environ:
    print(data)
    print('_'*15)
    print(os.environ[data])
    print('='*30)
    