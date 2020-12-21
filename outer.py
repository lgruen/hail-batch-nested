import os

import hailtop.batch as hb 

backend = hb.ServiceBackend(
    billing_project='leonhardgruenschloss-trial',
    bucket='leo-tmp-au')

b = hb.Batch(backend=backend, name='outer') 

j = b.new_job(name='launch-inner')
j.image(f'gcr.io/{os.getenv("GCP_PROJECT")}/hail-batch-nested:latest')
j.command('python3 inner.py')

b.run()
