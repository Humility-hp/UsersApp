items=['greet','anger','stupidity']
list_items=['welcome','hello','Afternoon','madness','furious','barefeeted','no self-control','bad manners']
for salute in items:
 if salute=='greet':
  for rep in list_items[:3]:
   print(f'{salute}={rep}')
 elif salute == 'anger':
  for rep in list_items[3:5]:
   print(rep)
 else:
  for rep in list_items[5:8]:
   print(rep) 
 print('finally')
