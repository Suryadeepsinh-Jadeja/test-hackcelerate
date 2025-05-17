import requests

# === Google Images ===
def get_google_image_urls(celebrity_name, total_num=20):
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
            'num': min(10, total_num - len(all_image_urls)),
            'start': start_index
        }

        response = requests.get(url, params=params).json()
        items = response.get('items', [])
        if not items:
            break

        image_urls = [item['link'] for item in items]
        all_image_urls.extend(image_urls)

        if len(all_image_urls) >= total_num:
            break

    return all_image_urls

# === YouTube Videos ===
def get_youtube_video_urls(query, max_results=10):
    api_key = 'AIzaSyBkORAF1uQ8gm7HUu5dzF6qRHOkkxkmA1s'
    url = 'https://www.googleapis.com/youtube/v3/search'

    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': max_results,
        'key': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'items' not in data:
        return []

    video_urls = [f"https://www.youtube.com/watch?v={item['id']['videoId']}" for item in data['items']]
    return video_urls

# === Vimeo Videos ===
def get_vimeo_video_urls(query, max_results=10):
    VIMEO_TOKEN = '12397fab507f50671d13d5a1ca022c36'  # Replace with valid token
    headers = {
        'Authorization': f'Bearer {VIMEO_TOKEN}'
    }

    params = {
        'query': query,
        'per_page': max_results,
        'sort': 'relevant',
        'direction': 'desc'
    }

    url = 'https://api.vimeo.com/videos'

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if 'data' not in data or not data['data']:
            print("No Vimeo videos found.")
            return []

        return [video['link'] for video in data['data']]

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error (Vimeo): {http_err}")
    except Exception as err:
        print(f"Other error (Vimeo): {err}")

    return []

# === Dailymotion Videos ===
def get_dailymotion_video_urls(query, max_results=10):
    url = "https://api.dailymotion.com/videos"
    params = {
        'search': query,
        'limit': max_results,
        'fields': 'title,url'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if 'list' not in data or not data['list']:
            print("No Dailymotion videos found.")
            return []

        return [video['url'] for video in data['list']]

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error (Dailymotion): {http_err}")
    except Exception as err:
        print(f"Other error (Dailymotion): {err}")

    return []

# === MAIN ===

if __name__ == "__main__":
    search_term = input("Enter your search term: ").strip()
    num_images = int(input("How many image URLs do you want? "))
    num_videos = int(input("How many video URLs do you want per platform (YouTube, Vimeo, Dailymotion)? "))

    # Google Images
    print(f"\n📸 Fetching {num_images} Image URLs for: {search_term}\n")
    images = get_google_image_urls(search_term, total_num=num_images)
    for i, url in enumerate(images, 1):
        print(f"{i}. {url}")

    # YouTube Videos
    print(f"\n▶️ Fetching {num_videos} YouTube Video URLs for: {search_term}\n")
    youtube_videos = get_youtube_video_urls(search_term, max_results=num_videos)
    for i, url in enumerate(youtube_videos, 1):
        print(f"{i}. {url}")

    # Vimeo Videos
    print(f"\n🎬 Fetching {num_videos} Vimeo Video URLs for: {search_term}\n")
    vimeo_videos = get_vimeo_video_urls(search_term, max_results=num_videos)
    for i, url in enumerate(vimeo_videos, 1):
        print(f"{i}. {url}")

    # Dailymotion Videos
    print(f"\n📹 Fetching {num_videos} Dailymotion Video URLs for: {search_term}\n")
    dailymotion_videos = get_dailymotion_video_urls(search_term, max_results=num_videos)
    for i, url in enumerate(dailymotion_videos, 1):
        print(f"{i}. {url}")
