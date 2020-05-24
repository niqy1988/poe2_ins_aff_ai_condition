import uuid

NAMESPACE_PREFIX = 'mod.poe2.ins_aff_ai_condition.'

def get_uuid(debug_name: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, NAMESPACE_PREFIX + debug_name))

print(get_uuid('abv'))