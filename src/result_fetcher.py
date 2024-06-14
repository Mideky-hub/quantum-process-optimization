from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService(
    channel='ibm_quantum',
    instance='ibm-q/open/main',
    token='YOUR_API_TOKEN'
)

current_ongoing_jobs = [
    'csp4wsvvwqp0008b49tg',
    'csp4wsk1k2e0008p7qdg',
    'csp4wsb1k2e0008p7qd0'
]

for job_id in current_ongoing_jobs:
    job = service.job(job_id)
    job_result = job.result()
    for idx, pub_result in enumerate(job_result):
        print(f"Expectation values for pub {idx}: {pub_result.data.evs}")