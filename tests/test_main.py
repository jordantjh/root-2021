from unittest import mock
from models.ProcessDrives import ProcessDrives


def test_main(mocker):
    """ 
    Ensure execute() is run in order to process the files
    """
    import main
    execute_mock = mocker.patch.object(ProcessDrives, 'execute')
    main.main()  # run the main function
    execute_mock.assert_called_once()


def test_init():
    """
    Ensure init() has a __name__ == __main__ check
    and inside it, runs the main function wrapped in a system exit
    """
    import main
    with mock.patch.object(main, "main", return_value=42):
        with mock.patch.object(main, "__name__", "__main__"):
            with mock.patch.object(main.sys, 'exit') as mock_exit:
                main.init()
                assert mock_exit.call_args[0][0] == 42
