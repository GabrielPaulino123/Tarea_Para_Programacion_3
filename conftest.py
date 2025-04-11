import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Esto obtiene el resultado de la prueba
    outcome = yield
    rep = outcome.get_result()


    if rep.when == "call" and rep.failed:
        driver = item.funcargs['setup']
        screenshot_path = "fallo_captura.png"
        driver.save_screenshot(screenshot_path)


        if screenshot_path:
            extra = getattr(rep, 'extra', [])
            extra.append(pytest_html.extras.png(screenshot_path))
            rep.extra = extra


def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')
