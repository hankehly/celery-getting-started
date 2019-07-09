broker_url = 'redis://redis'
result_backend = 'redis://redis'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Tokyo'
enable_utc = True

task_annotations = {
    'tasks.add': {
        'rate_limit': '10/m'
    }
}
