import uuid
import xml
import json
import yaml
import shutil

from stringtable import StringTable
from gamedatabundle import GameDataBundle

# load all config files
config = {}
with open('config/general.yaml') as general_config_file:
    config['general'] = yaml.safe_load(general_config_file)
for type in config['general']['effect_type']:
    with open(f'config/{type}.yaml') as type_config_file:
        config[type] = yaml.load(type_config_file, Loader=yaml.BaseLoader)

# create string table
string_table = StringTable('game\customai', 17301)

# generate configurations for inspiration and affliction
for effect_subject_key, effect_subject in config['general']['effect_subject'].items():
    for effect_type_key, effect_type in config['general']['effect_type'].items():
        # get effect category
        category_name = '{effect_subject_key}_{effect_type_key}'.format(
            effect_subject_key=effect_subject_key,
            effect_type_key=effect_type_key,
        )
        category_uuid = config['general']['effect_category'][category_name]['uuid']

        # create a game data bundle for this category
        game_data_bundle = GameDataBundle()

        # insert relevant effects
        for attribute_key, attribute in config['general']['attribute'].items():
            for attribute_effect in config[effect_type_key]['attribute_effect'][attribute_key]:
                # generate debug_name and descriptive text
                debug_name = '{subject}_{type}_{attribute}_{tier}'.format(
                    subject=effect_subject_key,
                    type=effect_type_key,
                    attribute=attribute_key,
                    tier=attribute_effect['tier']
                ).upper()
                display_name = '{subject}: Has {type} - {attribute} T{tier} ({description})'.format(
                    subject=effect_subject['description'],
                    type=effect_type['description'],
                    attribute=attribute['description'],
                    tier=attribute_effect['tier'],
                    description=attribute_effect['description'],
                )
                display_name_id = string_table.insert(display_name)
                print(debug_name)
                print(display_name)
                print(display_name_id)

                # add effect to game_data_bundle
                game_data_bundle.insert_ins_aff(
                    debug_name,
                    display_name_id,
                    effect_subject['uuid'],
                    attribute_effect['uuid'],
                    category_uuid
                )

        # output game_data_bundle
        game_data_bundle_file_path = 'output/new_{subject}_{type}_conditions.gamedatabundle'.format(
            subject = effect_subject_key,
            type = effect_type_key,
        )
        game_data_bundle.write(game_data_bundle_file_path)

# output string table
string_table_file_path = 'output/localized/en/text/game/customai.stringtable'
string_table.write(string_table_file_path)

# output manifest.json
shutil.copyfile('template/manifest.json', 'output/manifest.json')