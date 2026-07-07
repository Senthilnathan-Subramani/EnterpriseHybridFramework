class Authentication:
    def bearer(self,token):
        return {'Authorization':'Bearer '+token}
