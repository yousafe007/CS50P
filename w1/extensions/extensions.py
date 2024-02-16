mime_types = {
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.zip': 'application/zip'
}

unknownFile = True
user_input = input('File name: ').strip().lower()
for key, value in mime_types.items():
    if user_input.endswith(key):
        print(value)
        unknownFile = False
        break

if (unknownFile):
    print('application/octet-stream')
