class JsonService:
    """
            JsonService takes care of serialization-related functions, such as converting objects to
            dictionaries, in order to make them serializable.

            Methods:
                prepareModel
    """
    @staticmethod
    def prepareModel(instance):
        """
        Turns a model instance into a dictionary ready for serialization

        Examples:
            - To serialize a model instance
                user = User(...)
                userDict = JsonService.prepareModel(user)

        :param instance: SQLAlchemy.Model
        :return: dict
        """
        serialization = {}
        for c in instance.__table__.columns:
            value = getattr(instance, c.name)
            try:
                json.dumps(value)
            except:
                value = str(value)

            serialization[c.name] = value

        return serialization
