from main import app
class TestClass(object):
    def setup_class(self):
        self.app = app.test_client()
    def test_ffp(self):
        rv = self.app.get('/https://raw.githubusercontent.com/YUX-IO/ffp/master/test')
        assert rv.status_code == 200
        assert rv.data == b'https://github.com/YUX-IO/ffp'
    def test_ffp_r(self):
        rv = self.app.get('/r/https://raw.githubusercontent.com/YUX-IO/ffp/master/test')
        assert rv.status_code == 200
        assert rv.data == b'https://127.0.0.1:5000/https://github.com/YUX-IO/ffp'