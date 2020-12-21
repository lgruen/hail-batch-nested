To compile the Docker image that launches the *inner* batch, set the
`GCP_PROJECT` environment variable and then run `make`.

To be able to successfully submit the the *outer* batch that launches the
*inner* batch, the outer's container image must have access to the session ID
token. Currently, this requires setting `mount_tokens=True` when creating the
main job:
https://github.com/hail-is/hail/blob/main/hail/python/hailtop/batch/backend.py#L479

The Docker image currently symlinks `/user-tokens/tokens.json` to
`~/.hail/tokens.json`. That's a workaround related to DNS resolution. When
using `location = "gce"` in `/deploy-config/deploy-config.json`, we could use
the `/user-tokens/tokens.json` path directly. However, that causes the
"internal" `batch.hail` DNS to be used. The job's container image can't resolve
that using Cloud DNS (whereas the worker VM can).  Using `location =
"external"` causes the full domain to be used, which can be resolved from the
container. However, that also requires the token to be present at
`~/.hail/tokens.json`.
