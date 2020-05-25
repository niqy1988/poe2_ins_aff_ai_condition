import uuid
import xml
import json
import yaml
from stringtable import StringTable

# load all config files
configs = {}
with open('config/general.yaml') as general_config_file:
    configs['general'] = yaml.safe_load(general_config_file)
with open('configs/inspiration.yaml') as inspiration_config_file:
    configs['inspiration'] = yaml.load(inspiration_config_file, Loader=yaml.BaseLoader)
with open('configs/affliction.yaml') as affliction_config_file:
    configs['affliction'] = yaml.load(affliction_config_file, Loader=yaml.BaseLoader)


# uuid generating function
def get_uuid(debug_name: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, '{0}.{1}'.format(
        configs['general']['uuid_namespace_prefix'], debug_name
    )))


# generating configuration for self inspirations

print('{0}.{1}'.format(
    configs['general']['uuid_namespace_prefix'], 'abb'
))
print(get_uuid('abv'))
print(get_uuid('abb'))
print(get_uuid('abb'))
print(get_uuid('abv'))

a = StringTable('game\customai', 17301)
print(a.insert_entry('some text'))
print(a.insert_entry('some other texts'))
print(a.insert_entry('a third entry'))

a.write('output/output.xml')
