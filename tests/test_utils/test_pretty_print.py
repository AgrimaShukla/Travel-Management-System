from utils.pretty_print import data_tabulate

def test_data_tabulate(capsys):
    data = [('Agrima', '21', 'agrima@gmail.com')]
    headers = ('Name', 'Age', 'Email')
    data_tabulate(data, headers)
    captured = capsys.readouterr()
    assert 'Agrima' in captured.out
