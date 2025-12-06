from playwright.sync_api import Page


def mock_static_resourses(page: Page) -> None:
    page.route("**/*.{ico,png,jpj,svg,webp,mp3,mp4,woff,woff2}", lambda route: route.abort())
