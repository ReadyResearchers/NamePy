"""A program to test the command line interface of NamePy."""

from typer.testing import CliRunner

from src.CLI import app

runner = CliRunner()

def test_find_vars_cli():
    """Test that CLI returns correct number of assignment statements."""
    result = runner.invoke(app, ["find-vars", "./test_files"])
    assert result.exit_code == 0
    assert "{'__init__.py': 0, 'test_file.py': 6}" in result.stdout


def test_find_var_len_cli():
    """Test that CLI returns correct number of assignment statements."""
    result = runner.invoke(app, ["find-var-len", "./test_files"])
    assert result.exit_code == 0
    assert "1" in result.stdout
