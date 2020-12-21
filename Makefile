docker:
	docker build -t gcr.io/${GCP_PROJECT}/hail-batch-nested:latest .
	docker push gcr.io/${GCP_PROJECT}/hail-batch-nested:latest
