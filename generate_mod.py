import uuid
import xml
import json
import yaml

from stringtable import StringTable
from gamedatabundle import GameDataBundle


# load all config files
config = {}
with open('config/general.yaml') as general_config_file:
    config['general'] = yaml.safe_load(general_config_file)
with open('config/inspiration.yaml') as inspiration_config_file:
    config['inspiration'] = yaml.load(inspiration_config_file, Loader=yaml.BaseLoader)
with open('config/affliction.yaml') as affliction_config_file:
    config['affliction'] = yaml.load(affliction_config_file, Loader=yaml.BaseLoader)


# generate configuration for self inspirations
condition_subject = 'self'
condition_type = 'inspiration'
category_name = f'{condition_subject}_{condition_type}'
subject_uuid = config['general']['system_uuid']['condition_subject'][condition_subject]
category_uuid = config['general']['system_uuid']['condition_category'][category_name]

game_data_bundle = GameDataBundle()
game_data_bundle.insert_ins_aff('test_cond', 123, subject_uuid, [subject_uuid, category_uuid], category_uuid)
game_data_bundle.insert_ins_aff('test_cond2', 321, category_uuid, [category_uuid, subject_uuid], subject_uuid)
game_data_bundle.write('output/gamedata/bundle.json')

print(subject_uuid)
print(category_uuid)

a = StringTable('game\customai', 17301)
print(a.insert('some text'))
print(a.insert('some other texts'))
print(a.insert('a third entry'))
# a.write('output/dir/another/output.xml')
