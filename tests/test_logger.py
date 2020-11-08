import os
import logging

from app.logger_helper import get_logger, change_logger_location


def test_create_log(capsys, caplog):
    """
    Test create log
    """
    src_path = os.path.dirname(os.path.realpath(__file__))
    log_file_0 = f"{src_path}/out_0.log"
    log_file_1 = f"{src_path}/out_1.log"
    # Delete file
    try:
        os.remove(log_file_0)
        os.remove(log_file_1)
    except Exception:
        pass
    # No logs exists
    assert not os.path.isfile(log_file_0)
    assert not os.path.isfile(log_file_1)
    # Create log and write
    logger = get_logger(log_file_0, log_file_flag=True)
    logger.info("Hola Mundo")
    # Check format
    captured = capsys.readouterr()
    assert "|INFO|root|test_create_log|Hola Mundo\n" in captured.out
    assert [("root", logging.INFO, "Hola Mundo")] == caplog.record_tuples
    # change file
    change_logger_location(logger, log_file_1)
    logger.info("Hola Mundo, desde el otro archivo")
    # Log file created
    assert os.path.isfile(log_file_0)
    assert os.path.isfile(log_file_1)
    # Delete file
    os.remove(log_file_0)
    os.remove(log_file_1)
    # No logs exists
    assert os.path.isfile(log_file_0) is False
    assert os.path.isfile(log_file_1) is False
