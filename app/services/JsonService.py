class JsonService:
    @staticmethod
    def prepareModel(instance):
        serialization = {}
        for c in instance.__table__.columns:
            value = getattr(instance, c.name)
            try:
                json.dumps(value)
            except:
                value = str(value)

            serialization[c.name] = value

        return serialization
