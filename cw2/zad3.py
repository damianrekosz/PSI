from datetime import datetime
print('{:%Y-%m-%d %H:%M}'.format(datetime(2019, 10, 10, 10, 26)))
print('{} {}'.format(23, 67))
print('{:>20}'.format('testetst'))
print('{:_<20}'.format('testetst'))
print('{:010.4f}'.format(4.43566456))