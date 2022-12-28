import traceback
import re

def exception(trace):
    file_name = "main.py"
    line = re.search("line \d+", trace.split("\n")[1]).group(0)[5:]
    exception = trace.split("\n")[-2].strip()
    print("Ошибка в строке", line,  tree[file_name + ' ' + line][exception][hash(trace)])
if __name__ == '__main__':
    errors = [["main.py 31", "TimeoutError",
            "Traceback (most recent call last):\n  File \"main.py\", line 31, in <module>\n    raise TimeoutError()\nTimeoutError\n",
            "Время ожидания истекло"],
            ["main.py 35", "KeyError",
            "Traceback (most recent call last):\n  File \"main.py\", line 35, in <module>\n    raise KeyError()\nKeyError\n",
            "Ключ, указанный вами, не найден"],
            ["main.py 39", "TypeError",
            "Traceback (most recent call last):\n  File \"main.py\", line 39, in <module>\n    raise TypeError()\nTypeError\n",
            "Неверный тип данных"],
            ["main.py 43", "IndexError",
            "Traceback (most recent call last):\n  File \"main.py\", line 43, in <module>\n    raise IndexError()\nIndexError\n",
            "Индекс вышел за пределы последовательности"],
            ["main.py 47", "ImportError",
            "Traceback (most recent call last):\n  File \"main.py\", line 47, in <module>\n    raise ImportError()\nImportError\n",
            "Ошибка иморта библиотеки, попробуйте pip"]
            ]
    tree = {}
    for i in errors:
        tree[i[0]] = {i[1]:{hash(i[2]): i[3]}}

    try:
        raise TimeoutError()
    except:
        exception(traceback.format_exc())
    try:
        raise KeyError()
    except:
        exception(traceback.format_exc())
    try:
        raise TypeError()
    except:
        exception(traceback.format_exc())
    try:
        raise IndexError()
    except:
        exception(traceback.format_exc())
    try:
        raise ImportError()
    except:
        exception(traceback.format_exc())