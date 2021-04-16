# -*- coding: utf-8 -*-
from urllib.parse import urljoin

from flask_static_digest import FlaskStaticDigest


class WebpackFlaskStaticDigest(FlaskStaticDigest):
    """
    FLASK_WEBPACK_DEV_HOST
    """

    def init_app(self, app):
        self.webpack_dev_host = app.config.get("FLASK_WEBPACK_DEV_HOST")
        super().init_app(app)

    def static_url_for(self, endpoint, **values):
        if self.app.debug and self.webpack_dev_host:
            return self._prepend_webpack_dev_host_url(values.get('filename'))

        return super().static_url_for(endpoint, **values)

    def _prepend_webpack_dev_host_url(self, filename):
        return urljoin(self.webpack_dev_host, filename)
