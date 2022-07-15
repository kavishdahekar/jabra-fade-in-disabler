import os
import sys
import logging
import rumps

def get_bool_env_var(env_var, default_val=False):
    """
    deal with wierd return type of os.environ across
    python versions
    """
    val = os.environ.get('JABRA_DEVOLVE_DEBUG', False)
    if type(val) == bool:
        return val
    elif type(val) == str and val.lower() == 'true':
        return True
    else:
        return False

def init_logger():
    logging.basicConfig(
        level=logging.ERROR,
        format='*** %(asctime)s : %(levelname)-8s : %(message)s'
    )

    if get_bool_env_var('JABRA_DEVOLVE_DEBUG'):
        rumps.debug_mode(True)
        logging.getLogger().setLevel(logging.DEBUG)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("./jabra-fade-in-disabler")

    return os.path.join(base_path, relative_path)