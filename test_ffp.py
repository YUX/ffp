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
        assert rv.data == b'https://localhost/https://github.com/YUX-IO/ffp'
    def test_ffp_badge(self):
        rv = self.app.get('/https://img.shields.io/badge/ffp.yux.io-✔-green.svg')
        assert rv.status_code == 200
        assert rv.mimetype == 'image/svg+xml'