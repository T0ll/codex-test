from codex_test.cli import main


def test_main_smoke(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from codex-test!" in captured.out
