import uuid
from stringtable import StringTable

NAMESPACE_PREFIX = 'mod.poe2.ins_aff_ai_condition.'

def get_uuid(debug_name: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, NAMESPACE_PREFIX + debug_name))

print(get_uuid('abv'))

a = StringTable('game\customai', 17301)
print(a.insert_entry('some text'))
print(a.insert_entry('some other texts'))
print(a.insert_entry('a third entry'))

a.write('output/output.xml')
