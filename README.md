To compile the Docker image that launches the inner batch, set the
`GCP_PROJECT` environment variable and then run:

```shell
gcloud builds submit --tag gcr.io/$GCP_PROJECT/hail-batch-nested:latest
```

To be able to successfully submit the outer batch that launches the inner
batch, the outer's container image must have access to the session ID token.
Currently, this requires setting `mount_tokens=True` when [creating] the main
job.

[creating]: https://github.com/hail-is/hail/blob/main/hail/python/hailtop/batch/backend.py#L479

The Docker image currently symlinks `/user-tokens/tokens.json` to
`~/.hail/tokens.json`. That's a workaround related to user containers currently
not being allowed to send traffic to the internal gateway (blocked using
[iptables] for the "public" network). Both the worker VM and container can
reach the internal gateway, but not the user container. Setting `location =
"gce"` in `/deploy-config/deploy-config.json` would allow us to use the
`/user-tokens/tokens.json` path. However, that causes the "internal"
`batch.hail` domain to be used. Instead, using `location = "external"` causes
the full domain to be used, which can be reached from the user container.
However, that requires the token to be present at `~/.hail/tokens.json`.

[iptables]: https://github.com/hail-is/hail/blob/main/batch/batch/driver/instance_pool.py#L318
