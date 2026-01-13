#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    ラムダ式sorted()を使ってartifactを'power'でソートする
    """

    return sorted(artifacts, key=lambda artifact: artifact['power'])


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """
    ラムダ式filter()を使ってmagesの'power'が'min_power'以上のものを検索する
    """

    return list(filter(lambda mage: min_power < mage['power'], mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    ラムダ式map()を使ってspellsの各要素を'*'で挟んで返す
    """

    return list(map(lambda spell: f"*{spell}*", spells))


def mage_stats(mages: list[dict]) -> dict:
    """
    ラムダ式max(), min(), sum()を使ってmagesで以下の情報を返す
    ・一番powerの高いmage
    ・一番powerの低いmage
    ・powerの平均値
    """

    super_mage = max(mages, key=lambda mage: mage['power'])
    noob_mage = min(mages, key=lambda mage: mage['power'])

    return {'max_power': super_mage['power'],
            'min_power': noob_mage['power'],
            'avg_power': round(sum(map(lambda mage: mage['power'], mages))
                               / len(mages), 2)}


def main() -> None:
    """
    ラムダ式関数実行関数
    """

    artifacts = [{'name': 'Wind Cloak', 'power': 104, 'type': 'armor'},
                 {'name': 'Crystal Orb', 'power': 78, 'type': 'relic'},
                 {'name': 'Fire Staff', 'power': 99, 'type': 'armor'},
                 {'name': 'Wind Cloak', 'power': 60, 'type': 'accessory'}]
    mages = [{'name': 'Nova', 'power': 89, 'element': 'shadow'},
             {'name': 'River', 'power': 73, 'element': 'light'},
             {'name': 'Ember', 'power': 96, 'element': 'water'},
             {'name': 'Luna', 'power': 86, 'element': 'lightning'},
             {'name': 'Rowan', 'power': 79, 'element': 'ice'}]
    spells = ['heal', 'freeze', 'earthquake', 'darkness']

    print("========lambda_spells.py========")
    print()

    # 1.aritifact_srterを実行
    print("Testing artifact sorter...")
    print(artifact_sorter(artifacts))
    print()

    # 2.power_filterを実行
    print("Testing power_filter...")
    print(power_filter(mages, 80))
    print()

    # 3.spell_transformerを実行
    print("Testing spell_transformer...")
    print(spell_transformer(spells))
    print()

    # 4.mage_statsを実行
    print("Testing mage_stats...")
    print(mage_stats(mages))
    print()


if __name__ == "__main__":
    main()
