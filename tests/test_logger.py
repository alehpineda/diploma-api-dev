import os
import logging

from datetime import datetime
from app.logger_helper import get_logger, change_logger_location


def log_delete(log_file_0, log_file_1):
    """ Delete log file """
    try:
        os.remove(log_file_0)
        os.remove(log_file_1)
    except Exception:
        pass


def log_path():
    """ log path """
    src_path = os.path.dirname(os.path.realpath(__file__))
    log_file_0 = f"{src_path}/out_0.log"
    log_file_1 = f"{src_path}/out_1.log"
    return (log_file_0, log_file_1)


def test_logs_file_stream(capsys, caplog):
    """
    Test create log
    """
    log_file_0, log_file_1 = log_path()  # logs file
    log_delete(log_file_0, log_file_1)  # delete logs
    # No logs exists
    assert not os.path.isfile(log_file_0)
    assert not os.path.isfile(log_file_1)
    # Create log and write
    logger = get_logger(log_file=log_file_0, log_file_flag=True)
    logger.info("Hola Mundo")
    # Check format
    captured = capsys.readouterr()
    assert "|INFO|root|test_logs_file_stream|Hola Mundo\n" in captured.out
    assert [("root", logging.INFO, "Hola Mundo")] == caplog.record_tuples
    # change file
    change_logger_location(logger, log_file_1)
    logger.info("Hola Mundo, desde el otro archivo")
    # Log file created
    assert os.path.isfile(log_file_0)
    assert os.path.isfile(log_file_1)

    log_delete(log_file_0, log_file_1)  # delete logs
    # No logs exists
    assert not os.path.isfile(log_file_0)
    assert not os.path.isfile(log_file_1)


def test_logs_stream_only(caplog, capsys):
    """ Only log stream """

    # Create log and write
    logger = get_logger()  # Logger default values
    logger.info("Hola Mundo")
    # Check format
    captured = capsys.readouterr()
    assert "|INFO|root|test_logs_stream_only|Hola Mundo\n" in captured.out
    assert [("root", logging.INFO, "Hola Mundo")] == caplog.record_tuples
    # test date format
    assert datetime.strptime([rec.asctime for rec in caplog.records][0], "%Y-%m-%d %H:%M:%S")
    # Check no log file is created
    assert not os.path.isfile("logger.log")


def test_create_log():
    assert not os.path.isfile("logger.log")
    logger = get_logger(log_file_flag=True)
    logger.info("Hola Mundo")
    assert os.path.isfile("logger.log")
    os.remove("logger.log")
    assert not os.path.isfile("logger.log")
