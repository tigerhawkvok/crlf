from test.conftest import Application
from test.fixture.directory import directory


def test_convert_crlf_to_lf_log_output(application: Application):
    # given
    with directory() as dir:
        dir.store('file.txt', 'line')
        # when
        output = application.run(dir(), ['file.txt'])
    # then
    assert output.text == "Corrected file file.txt\n"


def test_invoked_with_missing_file(application: Application):
    # given
    with directory() as dir:
        # when
        output = application.run(dir(), ['missing.txt'])
    # then
    assert output.error == """usage: crlf [-h] filename
crlf: error: file does not exist 'missing.txt'
"""
