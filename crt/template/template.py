import os
import uuid
import json
import logging

import lycanthropy
import _jsonnet

logger = logging.getLogger(__name__)


class Template(object):
    '''
    Dict like represeantation of rendered jsonnet template.
    Parameters:
        path: str Path to jsonnet or json template
        body: str Jsonnet or JSON string.
    '''
    def __init__(self, path=None, body=None):
        if ((path is not None and body is not None) or
           (path is None and body is None)):
            raise ValueError('Specify body or path (but not both)')
        if path is not None:
            with open(path, 'r') as infile:
                body = infile.read()
                logger.debug('Loading template from: %s', path)
        self.body = body

        # The native_callbacks dict makes these functions available
        # from within the template.  They are called like this:
        #    std.native('env')('PATH')
        self.native_callbacks = {
            'uuidgen': ((), self.uuidgen),
            'getenv': ((), self.getenv),
        }
        self.__dict__ = self._eval()

    def _eval(self):
        '''
        Evaluate template using the Jsonnet library.
        '''
        data = _jsonnet.evaluate_snippet(
            'template',
            self.body,
            native_callbacks=self.native_callbacks
        )
        return json.loads(data)

    def to_camel(self):
        '''
        Return copy of rendered dict with all keys converted to camelCase
        '''
        return lycanthropy.morph_dict(
            self.__dict__,
            lycanthropy.snake_to_camel
        )

    def to_pascal(self):
        '''
        Return copy of rendered dict with all keys converted to PascalCase
        '''
        return lycanthropy.morph_dict(
            self.__dict__,
            lycanthropy.snake_to_pascal
        )

    @staticmethod
    def uuidgen():
        '''
        Make UUID generation availble in templates.
        '''
        return str(uuid.uuid4())

    @staticmethod
    def getenv():
        '''
        Make environment varibales available in templates.
        '''
        return dict(os.environ)

    # Dict interface
    def iteritems(self):
        return self.__dict__.iteritems()

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict_):
        return self.__dict__(self.__dict__, dict_)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __unicode__(self):
        return unicode(repr(self.__dict__))
