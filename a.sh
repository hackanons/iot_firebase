url -H "Content-Type: application/json" \
     -H "Authorization: Bearer 01CCFEA41DC49B7BE0782BC9BE6F064" \
     -X POST "https://0f8e1764-5be5-4046-9fd9-80581ac4ea87.pushnotifications.pusher.com/publish_api/v1/instances/0f8e1764-5be5-4046-9fd9-80581ac4ea87/publishes" \
     -d '{"interests":["hello"],"fcm":{"notification":{"title":"Hello","body":"Hello, world!"}}}'
