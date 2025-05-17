import requests

def get_google_image_urls(celebrity_name, total_num=50):
    api_key = 'AIzaSyBkORAF1uQ8gm7HUu5dzF6qRHOkkxkmA1s'
    cx = '8526bb01ab72c4115'
    url = 'https://www.googleapis.com/customsearch/v1'

    all_image_urls = []
    for start_index in range(1, total_num + 1, 10):
        params = {
            'q': celebrity_name,
            'cx': cx,
            'key': api_key,
            'searchType': 'image',
            'num': min(10, total_num - len(all_image_urls)),  # max 10
            'start': start_index
        }

        response = requests.get(url, params=params).json()

        items = response.get('items', [])
        if not items:
            break  # no more results

        image_urls = [item['link'] for item in items]
        all_image_urls.extend(image_urls)

        if len(all_image_urls) >= total_num:
            break

        start_index += 101 

    return all_image_urls

# Example usage
images = get_google_image_urls("Tom Cruise deepfake", 20)
for url in images:
    print(url)
