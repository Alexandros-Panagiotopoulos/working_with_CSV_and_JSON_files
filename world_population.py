import json
from country_codes import get_country_code
import pygal
from pygal.style import RotateStyle

# Load data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Builde dictionairy for population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict ["Year"] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Group the countries into 3 population levels
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1 [cc] = pop
    elif pop < 1000000000:
        cc_pops_2 [cc] = pop
    else:
        cc_pops_3 [cc] = pop

# Show how many countries are in each level
print (len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm = pygal.maps.world.World()
wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World population 2010, by country'
wm.add('0-10M', cc_pops_1)
wm.add('10M-1B', cc_pops_2)
wm.add('>1B', cc_pops_3)

wm.render_to_file(' World populations.svg')
