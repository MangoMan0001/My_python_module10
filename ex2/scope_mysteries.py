#!/usr/bin/env python3
import random


def mage_counter() -> callable:
    """
    呼び出された回数をカウントする関数を作成して返す
    """

    counter = 0

    def nest_counter() -> int:
        """
        クロージャで記憶されたcounter変数をインクリメントして返す
        """

        nonlocal counter
        counter += 1
        return counter

    return nest_counter


def spell_accumulator(initial_power: int) -> callable:
    """
    初期値を設定後、変数に引数に足す関数を作成して返す
    """

    total_power = initial_power

    def nest_accumulator(add_power) -> int:
        """
        クロージャで記憶されたtotal_power変数にadd_powerを足して返す
        """

        nonlocal total_power
        total_power += add_power

        return total_power

    return nest_accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    """
    引数に武器を持ち、その武器をenchantment_typeにエンチャントする関数を作成して返す
    """

    e_type = enchantment_type

    def nest_enchantment(target_item: str) -> str:
        """
        target_itemにクロージャで記憶されたされたe_typeエンチャントを適用して返す
        """

        nonlocal e_type

        return f"{e_type} {target_item}"

    return nest_enchantment


def memory_vault() -> dict[str, callable]:
    """
    ・dictを作るstore関数
    ・dectからvalueを引っ張ってくるrecall関数を作成する
    """

    memory = {}

    def store(key: str, value: str) -> None:
        """
        keyとvalueをmemory: dictに設定する
        """

        nonlocal memory
        memory[key] = value

    def recall(key: str) -> str:
        """
        keyに合うvalueをmemory: dictから参照し返す
        なければ"Memory not found"を返す。
        """

        nonlocal memory
        try:
            value = memory[key]
        except KeyError:
            value = "Memory not found"

        return value

    return {'store': store,
            'recall': recall}


def main() -> None:
    """
    ラムダ式関数実行関数
    """

    initial_powers = [43, 76, 52]
    power_additions = [11, 14, 20, 7, 9]
    enchantment_types = ['Frozen', 'Flaming', 'Shocking']
    items_to_enchant = ['Armor', 'Ring', 'Staff', 'Shield']

    print("========scope_mysteries.py========")
    print()

    # 1.mage_counterを実行
    r = 5
    counts = []
    result = mage_counter()

    print("Testing mage_counter...")
    for _ in range(r):
        counts.append(result())
    print(f"Total Call: {r}")
    print(counts)
    print()

    # 2.spell_accumulatorを実行
    initial = random.choice(initial_powers)
    additional = random.choice(power_additions)
    result = spell_accumulator(initial)

    print("Testing spell_accumulator...")
    print(f"inital: {initial}  additional: {additional}")
    print(f"Total Power: {result(additional)}")
    print()

    # 3.enchantment_factoryを実行
    print("Testing enchantment_factory...")

    e_type = random.choice(enchantment_types)
    item = random.choice(items_to_enchant)
    result_a = enchantment_factory(e_type)
    print(result_a(item))

    e_type = random.choice(enchantment_types)
    item = random.choice(items_to_enchant)
    result_b = enchantment_factory(e_type)
    print(result_b(item))
    print()

    # 4.memory_vaultを実行
    result = memory_vault()
    store = result['store']
    recall = result['recall']

    print("Testing memory_vault...")
    store('keep', 'going')
    print(f"keep {recall('keep')}!")
    print(f"keep {recall('just')}!")


if __name__ == "__main__":
    main()
