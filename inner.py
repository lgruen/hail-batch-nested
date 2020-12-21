import hailtop.batch as hb 

backend = hb.ServiceBackend(
    billing_project='leonhardgruenschloss-trial',
    bucket='leo-tmp-au')

b = hb.Batch(backend=backend, name='inner') 

j = b.new_job(name='hello') 
j.command('echo "hello world"') 

b.run()
