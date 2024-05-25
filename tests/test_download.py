import os
import unittest
from unittest.mock import patch, MagicMock
from downloader.download import baixar_video,baixar_videos

class TestDownload(unittest.TestCase):

        @patch('video_manager.download.YouTube')
        def test_baixar_video(self, MockYouTube):
                mock_yt = MockYouTube.return_value
                mock_stream = mock_yt.streams.get_highest_resolution.return_value
                mock_stream.download.return_value = None

                url = "https://www.youtube.com/watch?v=example"
                baixar_video(url,caminho_destino= 'test_videos')
                self.assertTrue(os.path.exists('test_videos'))

                mock_yt.streams.get_highest_resolution.assert_called_once()
                mock_stream.download.assert_called_once_with('test_videos')

        @patch('video_manager.download.YouTube')
        def test_baixar_videos(self, MockYouTube):
                mock_yt = MockYouTube.return_value
                mock_stream = mock_yt.streams.get_highest_resolution.return_value
                mock_stream.download.return_value = None

                urls = [
                        "https://www.youtube.com/watch?v=example1",
                        "https://www.youtube.com/watch?v=example2"
                ]
                baixar_videos(urls,caminho_destino= 'test_videos')

                self.assertEqual(mock_yt.streams.get_highest_resolution.call_count, 2)
                self.assertEqual(mock_stream.download.call_count, 2)

if __name__ == '__main__':
        unittest.main()