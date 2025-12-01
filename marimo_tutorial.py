import marimo

__generated_with = "0.18.1"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""
    From [Automate the Boring Stuff](https://automatetheboringstuff.com/3e/chapter5.html)
    """)
    return


@app.cell
def _():
    raise Exception('This is the error message.')
    return


@app.cell
def _():
    def box_print(symbol, width, height):
        if len(symbol) != 1:
            raise Exception('Symbol must be a single character string.')
        if width <= 2:
            raise Exception('Width must be greater than 2.')
        if height <= 2:
            raise Exception('Height must be greater than 2.')

        print(symbol * width)
        for i in range(height - 2):
            print(symbol + (' ' * (width - 2)) + symbol)
        print(symbol * width)

    try:
        box_print('*', 4, 4)
        box_print('O', 20, 5)
        box_print('x', 1, 3)
        box_print('ZZ', 3, 3)
    except Exception as err:
        print('An exception happened: ' + str(err))
    try:
        box_print('ZZ', 3, 3)
    except Exception as err:
        print('An exception happened: ' + str(err))
    return


@app.cell
def _():
    ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
    ages.sort()
    ages
    return (ages,)


@app.cell
def _(ages):
    assert ages[0] <= ages[-1]
    return


@app.cell
def _():
    ages_rev = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
    ages_rev.reverse()
    ages_rev
    return (ages_rev,)


@app.cell
def _(ages_rev):
    assert ages_rev[0] <= ages_rev[-1]
    return


@app.cell
def _():
    import logging
    return (logging,)


@app.cell
def _(logging):
    logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
        format=' %(asctime)s -%(levelname)s - %(message)s')
    return


@app.cell
def _(logging):

    logging.debug('Start of program')

    def factorial(n):
        logging.debug('Start of factorial(' + str(n) + ')')
        total = 1
        for i in range(1, n + 1):
            total *= i
            logging.debug('i is ' + str(i) + ', total is ' + str(total))
        logging.debug('End of factorial(' + str(n) + ')')
        return total

    print(factorial(5))
    logging.debug('End of program')
    return


@app.cell
def _():
    from pathlib import Path
    return (Path,)


@app.cell
def _(Path):
    Path('spam', 'bacon', 'eggs')
    return


@app.cell
def _(Path):
    str(Path('spam', 'bacon', 'eggs'))
    return


@app.cell
def _(Path):
    my_files = ['accounts.txt', 'details.csv', 'invite.docx']
    for filename in my_files:
        print(Path(r'C:\Users\Al', filename))
    return


@app.cell
def _(Path):
    Path('spam') / 'bacon' / 'eggs'
    return


@app.cell
def _(Path):
    Path('spam') / Path('bacon/eggs')
    return


@app.cell
def _(Path):
    Path.cwd()
    return


@app.cell
def _(Path):
    Path.home()
    return


@app.cell
def _(Path):
    Path.cwd()
    return


@app.cell
def _(Path):
    Path.cwd().is_absolute()
    return


@app.cell
def _(Path):
    Path('my/relative/path')
    return


@app.cell
def _(Path):
    Path.cwd() / Path('my/relative/path')
    return


@app.cell
def _(Path):
    Path.cwd()
    return


@app.cell
def _(Path):
    p = Path.cwd() / Path('my/relative/path/spam.txt')
    return (p,)


@app.cell
def _(p):
    p.anchor
    return


@app.cell
def _(p):
    p.parent
    return


@app.cell
def _(p):
    p.name
    return


@app.cell
def _(p):
    p.stem
    return


@app.cell
def _(p):
    p.suffix
    return


@app.cell
def _(p):
    p.drive
    return


@app.cell
def _(p):
    p.parts
    return


@app.cell
def _(p):
    p.parts[3]
    return


@app.cell
def _(p):
    p.parts[0:2]
    return


@app.cell
def _(Path):
    Path.cwd().parents[1]
    return


@app.cell
def _(Path):
    calc_file = Path('C:/Windows/System32/calc.exe')
    return (calc_file,)


@app.cell
def _(calc_file):
    calc_file.stat()
    return


@app.cell
def _(calc_file):
    calc_file.stat().st_mtime
    return


@app.cell
def _():
    import time
    return (time,)


@app.cell
def _(calc_file, time):
    time.asctime(time.localtime(calc_file.stat().st_mtime))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
