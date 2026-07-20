Analyze the Apache-style access log at `/app/access.log` and write a JSON report to
`/app/report.json`. The output must be a single JSON object.

Success criteria:

1. `/app/report.json` exists, is valid JSON, and has exactly the keys
   `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` is the number of non-empty log records in `/app/access.log`.
3. `unique_ips` is the number of distinct client IP addresses, where an address is
   the first whitespace-delimited field of a non-empty log record.
4. `top_path` is the request path that occurs most often in the log; extract a path
   from the request portion of each record (for example, `GET /path HTTP/1.1`).
