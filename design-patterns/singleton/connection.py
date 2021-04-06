# By using _ on the class name, it will not be imported implicitly to
# other modules if. It can only be imported explicitly.
class _Connection:
    def __init__(self):
        # Do some init stuff
        pass

    def __str__(self):
        return f"Connection, ID: {id(self)}"


_conn_instance = None


def Connection():
    global _conn_instance
    if _conn_instance is None:
        _conn_instance = _Connection()
    return _conn_instance
