from string import Template


_SERVERS_TO_ZONE = {
    "youth": "nluu1p",
    "geo": "nluu11p",
    "i-lab": "nluu5p",
    "dgk": "nluu9ot",
    "science": "nluu6p",
    "fsw": "nluu10p",
    "its": "nluu12p"
}

_SERVER_DESCRIPTIONS = {
    "youth": "YOUth Cohort Study",
    "geo": "Geosciences",
    "i-lab": "Humanities, Law, Economics, Governance, Open Societies",
    "dgk": "Veterinary Medicine, Medicine",
    "science": "Science",
    "fsw": "Social and Behavioral Sciences",
    "its": "University Corporate Offices"
}

_BASE_TEMPLATE = """{
    "irods_host": "${host}.data.uu.nl",
    "irods_port": 1247,
    "irods_home": "/${zone}/home",
    "irods_user_name": "${email_address}",
    "irods_default_resource": "irodsResc",
    "irods_zone_name": "${zone}",
    "irods_authentication_scheme": "pam",
    "irods_encryption_algorithm": "AES-256-CBC",
    "irods_encryption_key_size": 32,
    "irods_encryption_num_hash_rounds": 16,
    "irods_encryption_salt_size": 8,
    "irods_client_server_policy": "CS_NEG_REQUIRE",
    "irods_client_server_negotiation": "request_server_negotiation"
}
"""


class IBridgesUUTemplates():
    name = "Utrecht University templates"
    questions = ["email_address"]

    @staticmethod
    def list_templates():
        return [f"uu-{key: <7} - {_SERVER_DESCRIPTIONS[key]}" for key in _SERVERS_TO_ZONE]

    @staticmethod
    def contains(template_name):
        return template_name in ["uu-" + key for key in _SERVERS_TO_ZONE]

    @staticmethod
    def environment_json(template_name, email_address):
        host = template_name[3:]
        zone = _SERVERS_TO_ZONE[host]
        template = Template(_BASE_TEMPLATE)
        return template.substitute({"zone": zone, "email_address": email_address,
                                    "host": host})
