#!/usr/bin/env python3
import random


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """
    二つの引数で渡された関数を使う関数を作成して返す
    """

    if not callable(spell1) or not callable(spell2):
        raise TypeError("arg must be callable")

    return lambda: (spell1(), spell2())


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """
    base_spell実行時に返ってきた値にmaltiplierを乗算する関数を返す
    """

    if not callable(base_spell):
        raise TypeError("arg must be callable")

    return lambda: base_spell() * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    """
    二つの引数で渡された関数を使う関数を作成して返す
    作成された関数は引数を持ち、conditonとspell実行時に引数に渡す
    """

    if not callable(condition) or not callable(spell):
        raise TypeError("arg must be callable")

    return (lambda target: spell(target)
            if condition(target) else "Spell fizzled")


def spell_sequence(spells: list[callable]) -> callable:
    """
    リスト化された関数を順に実行する。
    作成された関数は引数を持ち、各関数実行時に引数に渡す
    """

    for spell in spells:
        if not callable(spell):
            raise TypeError("arg must be callable")

    return lambda value: [spell(value) for spell in spells]


def main() -> None:
    """
    ラムダ式関数実行関数
    """

    test_values = [14, 19, 25]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    spells = [lambda value: f"KAYAKUBOSHI (damage = {value})",
              lambda value: f"TABASUKOBOSHI (damage = {value})",
              lambda value: f"MAKIBISHIJIGOKU (damage = {value})"]

    print("========higher_magic.py========")
    print()

    # 1.spell_combinerを実行
    print("Testing spell_combiner...")
    result = spell_combiner(lambda: "Fireball hits Dragon",
                            lambda: " Heals Dragon")
    print(result())
    print()

    # 2.power_amplifierを実行
    print("Testing power_amplifier...")
    result = power_amplifier(lambda: 3, 3)
    print(result())
    print()

    # 3.conditional_casterを実行
    print("Testing conditional_caster...")
    result = conditional_caster(lambda target: True
                                if target != "Dragon" else False,
                                lambda target: "Fire ball" if target else None)
    print(result(random.choice(test_targets)))
    print()

    # 4.spell_sequenceを実行
    print("Testing spell_sequence...")
    result = spell_sequence(spells)
    print(result(random.choice(test_values)))
    print()


if __name__ == "__main__":
    main()
