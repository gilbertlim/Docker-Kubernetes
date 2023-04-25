from kubernetes import client, config

# pod 내부에 마운트된 sa token과 인증서 파일을 읽어 인증,인가 작업 수행
config.load_incluster_config()


try:
	print('Trying to list service..')
	# CoreV1 그룹의 API를 이용해 특정 네임스페이스의 서비스 목록 출력
	result = client.CoreV1Api().list_namespaced_service(namespace='default')
	for item in result.items:
		print('-> {}'.format(item.metadata.name))
except client.reset.ApiException as e:
	print(e)

print('----')

try:
	print('Trying to list pod..')
	result = client.CoreV1Api().list_namespaced_pod(namespace='default')
	for item in result.items:
			print(item.metadata.name)
except client.reset.ApiException as e:
	print(e)