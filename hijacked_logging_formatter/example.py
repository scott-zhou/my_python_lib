#!/usr/bin/env python

from hijacked_formatter import HijackedFormatter
import logging
import sys

logger = logging.getLogger()
fmt = '[CoreMW - TCG] %(asctime)s - %(filename)s:%(lineno)5d -%(levelname)8s - %(message)s'
formatter = HijackedFormatter(fmt)
stdout = logging.StreamHandler(sys.stdout)
stdout.setFormatter(formatter)
stdout.setLevel(logging.DEBUG)
logger.addHandler(stdout)
logger.setLevel(logging.DEBUG)

extra_keys = {
    HijackedFormatter.HIJACK_KEYWORD+'filename' : 'some_filename.py',
    HijackedFormatter.HIJACK_KEYWORD+'lineno' : 12345
}
logging.debug('log message', extra = extra_keys)
