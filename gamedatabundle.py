import os
import copy
import json
import yaml
import uuid

from typing import Optional, List

# load general config
with open('config/general.yaml') as general_config_file:
    general_config = yaml.safe_load(general_config_file)
    uuid_namespace_prefix = general_config['uuid_namespace_prefix']


# uuid generating function
def get_uuid(debug_name: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, '{0}.{1}'.format(
        uuid_namespace_prefix, debug_name
    )))


class GameDataBundle:
    gamedatabundle_dict = None
    gamedataobject_template = None
    conditional_component_template = None

    def __init__(self):
        # load template
        with open('template/gamedatabundle.json') as gamedatabundle_template_file:
            self.gamedatabundle_dict = json.load(gamedatabundle_template_file)
        with open('template/gamedataobject_ins_aff.json') as gamedataobject_template_file:
            self.gamedataobject_template = json.load(gamedataobject_template_file)
        with open('template/conditional_component.json') as conditional_component_template_file:
            self.conditional_component_template = json.load(conditional_component_template_file)

    def insert_ins_aff(self,
                       debug_name: str,
                       display_name_id: int,
                       subject_uuid: str,
                       effect_uuids: List[str],
                       category_uuid: str):

        # create new gamedataobject
        gamedataobject = copy.deepcopy(self.gamedataobject_template)
        gamedataobject['DebugName'] = debug_name
        gamedataobject['ID'] = get_uuid(debug_name)
        gamedataobject['Components'][0]['DisplayName'] = display_name_id
        gamedataobject['Components'][0]['AIConditionalCategoryID'] = category_uuid

        # insert identifier_uuid checks
        for se_uuid in effect_uuids:
            conditional_component = copy.deepcopy(self.conditional_component_template)
            conditional_component['Data']['Parameters'] = [
                subject_uuid, se_uuid
            ]
            gamedataobject['Components'][0]['ConditionalScripts']['Components'].append(
                conditional_component
            )

        # add gamedataobject to gamedatabundle
        self.gamedatabundle_dict['GameDataObjects'].append(gamedataobject)

    def write(self, file_path: str):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            json.dump(self.gamedatabundle_dict, f)


