def decode_base64_file(file_name, data):
    from django.core.files.base import ContentFile
    import base64

    if 'data:' in data and ';base64,' in data:
        header, data = data.split(';base64,')

        try:
            decoded_file = base64.b64decode(data)
        except TypeError:
            TypeError('invalid_image')

        return ContentFile(decoded_file, name=file_name)
    return None