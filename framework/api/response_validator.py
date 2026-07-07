class ResponseValidator:
    @staticmethod
    def status(resp,code):
        assert resp.status_code==code
