from geopy.adapters import AioHTTPAdapter
from geopy.extra.rate_limiter import AsyncRateLimiter
from geopy.geocoders import Nominatim

async with Nominatim(
    user_agent="specify_your_app_name_here",
    adapter_factory=AioHTTPAdapter,
) as geolocator:

    search = ["moscow", "paris", "berlin", "tokyo", "beijing"]
    geocode = AsyncRateLimiter(geolocator.geocode, min_delay_seconds=1)
    locations = [await geocode(s) for s in search]

    search = [
        (55.47, 37.32), (48.85, 2.35), (52.51, 13.38),
        (34.69, 139.40), (39.90, 116.39)
    ]
    reverse = AsyncRateLimiter(geolocator.reverse, min_delay_seconds=1)
    locations = [await reverse(s) for s in search]