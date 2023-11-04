import os
import pytest
import logging

def create_and_test_file(log):
    # Define your test logic that uses the temporary path
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    assert log.text.__contains__("message")


def test_temporary_path(caplog):
    # Call the function and pass the temporary path
    create_and_test_file(caplog)
