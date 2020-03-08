import asyncio
import unittest
from unittest.mock import patch, MagicMock
from utils.player_manager import PlayerManager


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)


class TestPlayerManager(unittest.TestCase):

    def setUp(self) -> None:
        self.url = "http://192.99.17.12:6410/"
        self.loop = asyncio.get_event_loop()
        self.player_manager = PlayerManager()

    @patch('utils.player_manager.PlayerManager.run_backup_file', new_callable=AsyncMock)
    @patch('utils.player_manager.PlayerManager.start_player_task', new_callable=AsyncMock)
    @patch('utils.player_manager.PlayerManager.auto_kill_player_task', new_callable=AsyncMock)
    def test_player_run(self,  mock_auto_kill_player_task, mock_player_start, mock_run_backup_file):
        """
        player executed
        player is started
        auto stop called
        """

        with patch.object(PlayerManager, 'is_started', return_value=True) as mock_is_started:
            self.loop.run_until_complete(self.player_manager.main_loop(url=self.url,
                                                                       auto_stop_seconds=5,
                                                                       backup_file_path="/tmp/fake",
                                                                       second_to_wait_before_check=2))
            mock_player_start.assert_called_with(self.url)
            mock_is_started.assert_called()
            mock_auto_kill_player_task.assert_called()
            mock_run_backup_file.assert_not_called()

    @patch('utils.player_manager.PlayerManager.start_player_task', new_callable=AsyncMock)
    @patch('utils.player_manager.PlayerManager.auto_kill_player_task', new_callable=AsyncMock)
    @patch('utils.player_manager.PlayerManager.run_backup_file', new_callable=AsyncMock)
    def test_player_run_and_failed(self, mock_run_backup_file, mock_auto_kill_player_task, mock_player_start):
        """
        player executed
        player not started
        run backup MP3 is called
        """
        with patch.object(PlayerManager, 'is_started', return_value=False) as mock_is_started:
            self.loop.run_until_complete(self.player_manager.main_loop(url=self.url,
                                                                       auto_stop_seconds=5,
                                                                       backup_file_path="/tmp/fake",
                                                                       second_to_wait_before_check=2))
            mock_player_start.assert_called_with(self.url)
            mock_is_started.assert_called()
            mock_run_backup_file.assert_called_with("/tmp/fake")
            mock_auto_kill_player_task.assert_called()


suite = unittest.TestSuite()
suite.addTest(TestPlayerManager("test_player_run_and_failed"))
runner = unittest.TextTestRunner()
runner.run(suite)
