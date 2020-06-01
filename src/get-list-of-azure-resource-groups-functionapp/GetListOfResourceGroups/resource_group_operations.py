import logging
import json
import os

from azure.mgmt.resource import ResourceManagementClient


def process_rg_instance(group):
    """
    Get the relevant pieces of information from a ResourceGroup instance.
    """
    return {
        "Name": group.name,
        "Id": group.id,
        "Location": group.location,
        "Tags": group.tags,
        "Properties": group.properties.provisioning_state \
            if group.properties and group.properties.provisioning_state else None
    }


async def list_rgs(credentials, subscription_id):
    """
    Get list of resource groups for the subscription id passed.
    """
    list_of_resource_groups = []

    with ResourceManagementClient(credentials, subscription_id) as rg_client:
        try:
            for i in rg_client.resource_groups.list():
                list_of_resource_groups.append(process_rg_instance(i))
                
        except Exception as e:
            logging.error("encountered: {0}".format(str(e)))

    return json.dumps(list_of_resource_groups)
