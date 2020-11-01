import asyncio
import os

import azure.functions as func
from azure.identity import DefaultAzureCredential
from .resource_group_operations import list_rgs


async def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    The main entry point to the function.
    """

    credentials = DefaultAzureCredential()
    subscription_id = os.environ.get(
        'AZURE_SUBSCRIPTION_ID', '11111111-1111-1111-1111-111111111111')

    list_of_rgs = await list_rgs(credentials, subscription_id)

    return func.HttpResponse(list_of_rgs, mimetype="application/json")
