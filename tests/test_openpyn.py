#!/usr/bin/env python3

import argparse
import datetime
import json
import logging
import logging.handlers
import sys
import time

import mock
import pytest

from openpyn import openpyn

# def test_version():
#     assert openpyn.__version__ == "2.7.0"


def test_list():
    with mock.patch('sys.argv', ['openpyn', '-l']):
        assert openpyn.main() == 0


def test_list_tor():
    with mock.patch('sys.argv', ['openpyn', '-l', '--tor']):
        assert openpyn.main() == 0


# def test_list_country():
#     with mock.patch('sys.argv', ['openpyn', '-l', 'au']):
#         assert openpyn.main() == 0
#
#
# def test_list_country_area_city():
#     with mock.patch('sys.argv', ['openpyn', '-l', 'au', '--area', 'adelaide']):
#         assert openpyn.main() == 0
#
#
# def test_list_country_area_state():
#     with mock.patch('sys.argv', ['openpyn', '-l', 'au', '--area', 'sa']):
#         assert openpyn.main() == 0


def test_list_country_area_state_p2p():
    with mock.patch('sys.argv', ['openpyn', '-l', 'au', '--area', 'sa', '--p2p']):
        assert openpyn.main() == 0


def test_connect_country_code():
    with mock.patch('sys.argv', ['openpyn', 'au', '--test']):
        assert openpyn.main() == 0


def test_connect_country_name():
    with mock.patch('sys.argv', ['openpyn', 'australia', '--test']):
        assert openpyn.main() == 0


def test_connect_country_code_arg():
    with mock.patch('sys.argv', ['openpyn', '-c', 'au', '--test']):
        assert openpyn.main() == 0


def test_connect_max_load():
    with mock.patch('sys.argv', ['openpyn', 'au', '-m', '50', '--test']):
        assert openpyn.main() == 0


def test_connect_top_servers():
    with mock.patch('sys.argv', ['openpyn', 'au', '-t', '5', '--test']):
        assert openpyn.main() == 0


def test_connect_pings():
    with mock.patch('sys.argv', ['openpyn', 'au', '-p', '5', '--test']):
        assert openpyn.main() == 0
