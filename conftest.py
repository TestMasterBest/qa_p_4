#!/usr/bin/env python
# -*- coding: utf-8   -*-
import pytest
from main import BooksCollector


@pytest.fixture
def collect():
    collect = BooksCollector()
    return collect