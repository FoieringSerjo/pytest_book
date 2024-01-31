from unittest import mock

import cards

from cards_cli_helper import cards_cli


def test_mock_version():
    with mock.patch.object(cards, "__version__", "1.2.3"):
        result = cards_cli("version")
        assert result == "1.2.3"
