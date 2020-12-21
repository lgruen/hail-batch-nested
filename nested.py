import hailtop.batch as hb 

backend = hb.ServiceBackend(
    billing_project='leonhardgruenschloss-trial',
    bucket='leo-tmp-au')

b = hb.Batch(backend=backend, name='test') 

j1 = b.new_job(name='hello') 
j1.command('echo "hello world"') 

j2 = b.new_job(name='check gsa') 
j2.command('ls -l /gsa-key/key.json') 

j3 = b.new_job(name='check user-token') 
j3.command('ls -l /user-tokens/tokens.json') 

j4 = b.new_job(name='check deploy-config') 
j4.command('ls -l /deploy-config/deploy-config.json') 

b.run()
