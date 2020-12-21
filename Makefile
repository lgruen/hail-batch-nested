docker:
	docker build -t gcr.io/${GCP_PROJECT}/hail-sub-batch:latest .
	docker push gcr.io/${GCP_PROJECT}/hail-sub-batch:latest
