import cPickle as pickle

from sqlobject import *

from model import hub
__connection__ = hub

__all__ = ['ObjectState', 'get_states_wrapper']

class ObjectState(SQLObject):
    """
    Class to implement a kind of vertical table over existing objects
    """
    class sqlmeta:
        table = 'ost_states'
    
    instance_id = IntCol()
    model_name = StringCol(length=50)
    name = StringCol(length=100)
    value = BLOBCol(length=2**24-1, varchar=False)
    
    _index = index.DatabaseIndex(model_name, instance_id, name, unique=True)
    
    pending = BoolCol(default=False)
    rejected = BoolCol(default=False)
    
    def _get_value(self):
        return pickle.loads(self._SO_get_value().decode('base64'))
    
    def _set_value(self, value):
        self._SO_set_value(pickle.dumps(value).encode('base64'))


class OSWrapper(dict):
    def __init__(self, model):
        self.model = model
    
    def _get_state(self, name):
        q = ObjectState.q
        sel = ObjectState.selectBy(model_name=self.model.__class__.__name__,
                                   instance_id=self.model.id, name=name)
        try:
            return sel[0]
        except IndexError:
            raise KeyError
    
    def __getitem__(self, item):
        state = self._get_state(item)
        return state.value
    
    def __setitem__(self, item, value):
        try:
            state = self._get_state(item)
            state.value = value
        except KeyError:
            ObjectState(instance_id=self.model.id, name=item, value=value,
                        model_name=self.model.__class__.__name__)
    
    def keys(self):
        states = ObjectState.selectBy(instance_id=self.model.id,
                                      model_name=self.model.__class__.__name__)
        return [i.name for i in states]
    
    def has_key(self, name):
        try:
            self._get_state(name)
            return True
        except KeyError:
            return False
    
    def approve(self, name):
        return self._get_state(name).approve()
    
    def reject(self, name):
        return self._get_state(name).reject()
    
    def get_history(self, name):
        return self._get_state(name).get_history()
    
    def get_modification_history(self, name):
        return self._get_state(name).get_modification_history()
    
    def get_pending_changes(self, name):
        return self._get_state(name).get_pending_changes()
    
    def get_rejected_changes(self, name):
        return self._get_state(name).get_rejected_changes()

def get_states_wrapper(self):
    return OSWrapper(self)
