import marimo

__generated_with = "0.18.1"
app = marimo.App()


@app.cell
def _():
    from pathlib import Path
    return (Path,)


@app.cell
def _(Path):
    p = Path('spam.txt')
    p.write_text('Hello, world!')
    return (p,)


@app.cell
def _(p):
    p.read_text()
    return


@app.cell
def _(Path):
    Path.cwd()
    return


@app.cell
def _(Path):
    hello_file = open(Path.cwd() / 'hello.txt', encoding= 'UTF-8')
    return (hello_file,)


@app.cell
def _(hello_file):
    hello_content = hello_file.read()
    hello_content
    return


@app.cell
def _(hello_file):
    hello_file.close()
    return


@app.cell
def _(Path):
    sonnet_file = open(Path.cwd() / 'sonnet29.txt', encoding='UTF-8')
    return (sonnet_file,)


@app.cell
def _(sonnet_file):
    sonnet_file.readlines()
    return


@app.cell
def _(sonnet_file):
    sonnet_file.close()
    return


@app.cell
def _():
    bacon_file = open('bacon.txt', 'w', encoding='UTF-8')
    bacon_file.write("Hello, world!\n")
    return (bacon_file,)


@app.cell
def _(bacon_file):
    bacon_file.close()
    return


@app.cell
def _():
    with open('data.txt', 'w', encoding='UTF-8') as file_obj:
        file_obj.write('Hello! World!')
    with open('data.txt', encoding='UTF-8') as file_obj:
        content = file_obj.read()
    return


@app.cell
def _():
    import shelve
    return (shelve,)


@app.cell
def _(shelve):
    shelf_file = shelve.open('mydata')

    shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon']
    shelf_file.close()
    return (shelf_file,)


@app.cell
def _(shelve):
    shelve.open('mydata')
    return


@app.cell
def _(shelf_file):
    type(shelf_file)
    return


@app.cell
def _(shelve):
    shelf_file2 = shelve.open('mydata')
    type(shelf_file2)
    return (shelf_file2,)


@app.cell
def _(shelf_file2):
    shelf_file2['cats']
    return


@app.cell
def _(shelf_file):
    shelf_file.close()
    return


@app.cell
def _(shelve):
    shelf_file3 = shelve.open('mydata')
    list(shelf_file3.keys())
    return (shelf_file3,)


@app.cell
def _(shelf_file3):
    list(shelf_file3.values())
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
