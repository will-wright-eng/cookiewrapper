import typer

from cgen import cli


def test_help():
    result = typer.testing.CliRunner().invoke(cli, "--help")
    assert result.exit_code == 0
    assert "Usage: cgen [OPTIONS] COMMAND [ARGS]..." in result.stdout
