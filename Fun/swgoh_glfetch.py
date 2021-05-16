import requests

legends = {'GRANDMASTERLUKE': {'value': 0, 'display': 'Grand Master Luke'}, 'SITHPALPATINE': {'value': 0, 'display': 'Sith Eternal Emperor'}, 'SUPREMELEADERKYLOREN': {'value': 0, 'display': 'Supreme Leader Kylo Ren'},  'GLREY': {'value': 0, 'display': 'Rey'}}

number_of_legends = 0

# guild_id = 11228
guild_id = input('Enter Guild ID: ')
resp = requests.get(f'http://swgoh.gg/api/guild/{guild_id}')
guild = resp.json()

for player in guild['players']:
    for unit in player['units']:
        name = unit['data']['base_id']
        if name in legends.keys():
            legends[name]['value'] += 1
            number_of_legends += 1

print('---')
for k, v in legends.items():
  print(f'{v["display"]} - {v["value"]}')
print(f'---\nTotal - {number_of_legends}')
