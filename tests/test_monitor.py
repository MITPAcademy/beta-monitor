import pytest
from monitor import check_discord_api, check_bot_discloud

def test_discord_api_status():
    status = check_discord_api()
    assert isinstance(status, bool)

def test_discloud_status():
    status = check_bot_discloud()
    assert isinstance(status, bool)