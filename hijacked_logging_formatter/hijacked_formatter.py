"""
Use HijackedFormatter instead of logging.Formatter for your Logger Handler
instance to overwrite the keys which is used by the logging system.
"""
import logging


class HijackedFormatter(logging.Formatter):
    """
    The extra argument (the dictionary which is used to populate the __dict__
    of the LogRecord) is not allow to clash with the keys used by the logging
    system. Which means you can not overwrite the those keys in logging module.

    HijackedFormatter is use for overwrite the keys which is used by the logging
    system.

    Use HijackedFormatter instead of logging.Formatter for your Logger Handler
    instance, and pass the keys which you want to overwrite in beginning with
    hijack keyword HijackedFormatter.HIJACK_KEYWORD

    For example, if you want to overwrite the filename and lineno, you can pass
    a dictionary like following:
    extra_keys = {
        HijackedFormatter.HIJACK_KEYWORD+'filename' : 'some_filename.py',
        HijackedFormatter.HIJACK_KEYWORD+'lineno' : 12345
    }
    logging.debug('log message', extra = extra_keys)
    """
    HIJACK_KEYWORD = 'hijack_'

    def format(self, record):
        hijacked_len = len(self.HIJACK_KEYWORD)
        newdict = {}
        for key in record.__dict__:
            if key.startswith(self.HIJACK_KEYWORD):
                hijacked_key = key[hijacked_len:]
                if len(hijacked_key) <= 0:
                    continue
                newdict[hijacked_key] = record.__dict__[key]
        record.__dict__.update(newdict)
        return logging.Formatter.format(self, record)
