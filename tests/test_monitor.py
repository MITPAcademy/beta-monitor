import pytest
from src.monitor import check_discord_api, check_bot_discloud
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_discord_api_status():
    status = check_discord_api()
    assert isinstance(status, bool)

def test_discloud_status():
    status = check_bot_discloud()
    assert isinstance(status, bool)