from string import ascii_lowercase as asc_lower
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
sng=input("")
if(check(sng)==True):
      print('yes')
else:
      print('no')
