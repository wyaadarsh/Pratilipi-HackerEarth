# Default dump file for state. Works only in single threaded operations
import base64
import traceback

import zlib

import dill as dill
from .exceptions import *
from logging import getLogger
from utils.db_utils import SessionManager

logger = getLogger(__name__)

DUMP_FILE = 'state.dump'


def get_order_object(game_id, starting_model=None):
    session = SessionManager()
    model = session.get_game_object(game_id)
    if not model:
        model = base64.standard_b64encode(zlib.compress(dill.dumps(starting_model())))
    return model


# Used to load file or connect to DB. Maintains State of Game by loading previous state
def load(resource=None, resource_accessor=None, resource_closer=None, *args, **kwargs):
    """
    Default loader
    resource: file or DB to connect to
    resource_accessor: function to access file or DB to read the dumped state.
                       can use *args and **kwargs to call the function
                       function should return the resource object
    resource_closer: function to close the connection or file.
                     Takes the resource object created by resource_accessor as input
    """
    if resource_accessor is None:
        resource_accessor = get_order_object
    if resource is None: resource = DUMP_FILE
    if resource_closer is None:
        resource_closer = lambda x: x
    fp = None
    try:
        fp = resource_accessor(resource, *args, **kwargs)
        if not fp:
            raise RequiredParamError("No session object found in DB.")
        model = dill.loads(zlib.decompress(base64.standard_b64decode(fp)))
        if model.user and model.user.session_obj:
            model.user.sync_session_obj()
            # TODO In future there may be attributes on user level also that may change
        logger.info("Loaded Node %s", model.id)
    except Exception as e:
        logger.error("Could not load resource %s, error: %s", resource, e)
        logger.error("Stacktrace: %s", traceback.print_exc())
        raise
    finally:
        if fp:
            resource_closer(fp)
    return model


def dump(id, obj):
    session = SessionManager()
    comp_obj = base64.standard_b64encode(zlib.compress(dill.dumps(obj)))
    session.update_insert_order_object(id, comp_obj)

