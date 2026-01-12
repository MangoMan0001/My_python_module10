#!/usr/bin/env python3
import random
import operator
import functools


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    spellsをoperationで指定された方法で一つの値にする
    add = 足し算
    multiply = 掛け算
    max = 最大値
    min = 最小値
    """

    op = {'add': operator.add,
          'multiply': operator.mul,
          'max': max,
          'min': min}

    return functools.reduce(op[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """
    base_enchantmentのpowerとelementを固定した新たな関数を作成する
     ’fire_enchant’, ’ice_enchant’, ’lightning_enchant’の3つを作成し、powerは50で固定
    """

    return {'fire_enchant':
            functools.partial(base_enchantment, power=50, element='fire'),
            'ice_enchant':
            functools.partial(base_enchantment, power=50, element='ice'),
            'lightning_enchant':
            functools.partial(base_enchantment, power=50, element='lightning')}


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    フィボナッチ数列を返す
    functools.lru_cacheを使って一度実行したことのある引数はメモリから参照される
    """

    if n <= 0:
        return 0
    if n == 1:
        return 1

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """
    @functools.singledispatch
    @spell.register()
    この二つのデコレータを使ってint, str, list型がきたときの処理を分けて実装する
    実装された関数を返す
    """

    # .仮に当てはまる型が定義されていなければ、ここで書いた関数が実行される
    @functools.singledispatch
    def spell(arg) -> str:
        """
        当てはまる型が実装されていない時に実行される
        """

        return "The spell was chanted."

    @spell.register(int)
    def _(arg) -> str:
        """
        int型の場合の処理
        """

        return f"The spell was chanted. Damage: {arg}"

    @spell.register(str)
    def _(arg) -> str:
        """
        str型の場合の処理
        """

        return f"The spell was chanted. Spell name: {arg}"

    @spell.register(list)
    def _(arg) -> str:
        """
        list型の場合の処理
        """

        return f"The spell was chanted. Spell count: {len(arg)}"

    return spell


def main() -> None:
    """
    ラムダ式関数実行関数
    """

    spell_powers = [25, 37, 30, 21, 26, 43]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [9, 8, 15]

    print("========functools_artifacts.py========")
    print()

    # 1.spell_reducerを実行
    print("Testing spell_reducer...")
    for op in operations:
        print(f"{op}: {spell_reducer(spell_powers, op)}")
    print()

    # 2.partial_enchanterを実行
    result = partial_enchanter(lambda power, element, target:
                                f"{element} -> {target} ({power})")
    elements = []
    elements.append(result['fire_enchant'])
    elements.append(result['ice_enchant'])
    elements.append(result['lightning_enchant'])
    print("Testing partial_enchanter...")
    for element in elements:
        print(element(target='enemy'))
    print()

    # 3.memoized_fibonacciを実行
    n = 10

    print("Testing memoized_fibonacci...")
    print(f"({n}): {memoized_fibonacci(n)}")
    print()

    # 4.spell_dispatcherを実行
    result = spell_dispatcher()

    print("Testing spell_dispatcher...")
    print(result({'spell': 5}))
    print(result(5))
    print(result('Fire ball'))
    print(result(['Fire ball', 'Ice age']))
    print()

if __name__ == "__main__":
    main()
