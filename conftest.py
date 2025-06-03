from config.config import load_config
from core.utils.api_client import get_token
from page_objects.page.serb_tests import SerbPage


@pytest.fixture()
def main_page(conf):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=100,
        )
        context = browser.new_context(
            viewport=conf.context.viewport_fhd,
        )
        page = context.new_page()
        yield page


@pytest.fixture()
def auth_serb(main_page, conf):
    main_page.goto(conf.urls.mmil)
    token = get_token()
    main_page.evaluate(
        """([token_key, token_value]) => {
            localStorage.setItem(token_key, token_value);
        }""",
        ["access", token]
    )
    main_page.reload()
    yield SerbPage(main_page)
