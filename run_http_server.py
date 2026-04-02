import os
from ads_mcp.coordinator import mcp
from ads_mcp.tools import search, core, get_resource_metadata  # noqa: F401
from ads_mcp.resources import (
    discovery, metrics, release_notes, segments
)  # noqa: F401

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
    )
```

**Then update the run command in App Platform to:**
```
sh -c 'echo "$GOOGLE_ADS_YAML" > google-ads.yaml && /workspace/.heroku/python/bin/python run_http_server.py'
