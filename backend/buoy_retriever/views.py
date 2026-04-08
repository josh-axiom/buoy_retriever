from datetime import datetime, timezone
from django.http import JsonResponse
from decouple import config
from urllib.parse import urljoin
import requests




ASSET_DOCS_API_BASE_URL = config(
    'ASSET_DOCS_API_BASE_URL',
    default='https://stage-asset-docs-postgrest.srv.axds.co/'
)


def get_asset_doc_list(request):

    ad_resp = requests.get(
        urljoin( ASSET_DOCS_API_BASE_URL, '/document'),
        params={
            "select": "uuid,label,data",
            "order": "created_at.desc",
            "limit": 10
        }
    )

    ad_resp.raise_for_status()

    ret = {
        "source": ASSET_DOCS_API_BASE_URL,
        "time": datetime.now( tz=timezone.utc ),
        "result": ad_resp.json(),
    }

    return JsonResponse( ret )