#!/usr/bin/env python3
import random
import functools
import time
from typing import Any


def spell_timer(func: callable) -> callable:
    """
    funcの実行時間を計測するデコレータ
    """

    @functools.wraps(func)
    def wrapper(*args, **kwards) -> Any:  # .可変長引数の書式はlistとdictのアンパック
        """
        funcの実行前後に実行時間の計算処理を増やした関数
        """

        print(f"Casting {func.__name__}...")
        start_time = time.time()

        result = func(*args, **kwards)

        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.4f} seconds")

        return result

    return wrapper


def power_validator(min_power: int) -> callable:
    """
    powerを引数として受け取る関数を受け取り、
    min_powerでバリデーションできるデコレータを作成する関数を作成する
    """

    def gen_decorator(func: callable) -> callable:
        """
        powerを引数として受け取る関数を受け取り、
        min_powerでバリデーションできるデコレータを作成する
        """

        @functools.wraps(func)
        def wrapper(*args, **kwards) -> Any:
            """
            受け取るpowerがmin_power以上かどうかバリデーションするラッパー関数
            """

            current_power = kwards.get('power')
            if not current_power:
                current_power = args[0]
            if current_power is not None and min_power <= current_power:
                return func(*args, **kwards)

            return "Insufficient power for this spell"

        return wrapper

    return gen_decorator


def retry_spell(max_attempts: int) -> callable:
    """
    呪文詠唱が失敗した場合にmax_attemptsまでリトライするデコレータを作成する関数を作成する
    """

    def gen_decorator(func: callable) -> callable:
        """
        func失敗後、max_attemptsまでリトライするデコレータを作成する
        """

        @functools.wraps(func)
        def wrapper(*args, **kwards) -> callable:
            """
            func失敗後、max_attemptsまでリトライするデコレータ
            """

            for i in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwards)

                    return result

                except Exception:
                    if i == max_attempts:
                        return ("Spell casting failed after "
                                f"{max_attempts} attempts")
                    print(f"Spell failed, retrying... "
                          f"(attempt {i}/{max_attempts})")

        return wrapper

    return gen_decorator


class MageGuild:
    """
    Mage登録クラス
    """

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        名前が正しいか
        Name is valid if it’s at least 3 characters
        and contains only letters/spaces
        """

        if 3 <= len(name) and all(c.isalpha() or c.isspace() for c in name):
            return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """
        魔力を使ってspell_nameを実行
        """

        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    """
    ラムダ式関数実行関数
    """

    test_powers = [9, 8, 10, 11]
    spell_names = ['shield', 'lightning', 'tornado', 'blizzard']
    mage_names = ['Alex', 'Ember', 'Zara', 'Luna', 'Nova', 'Jordan']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print("========functools_artifacts.py========")
    print()

    try:
        # 1.spell_timerを実行
        print("Testing spell_timer...")

        @spell_timer
        def fire_ball() -> str:
            """
            火の玉が打てる
            """

            time.sleep(0.5)
            return "Fireball cast!"

        result = fire_ball()
        print(f"Result: {result}")
        print()

        # 2.power_validataorを実行
        print("Testing power_validataor...")
        result = power_validator(10)

        @result
        def big_fire_ball(power) -> str:
            """
            魔力を使って火の玉を打つ
            """

            return f"({power}) BIG FIRE BALL!!!"

        for p in test_powers:
            print(f"power({p}): {big_fire_ball(p)}")
        print()

        # 3.retry_spellを実行
        print("Testing retry_spell...")
        result = retry_spell(5)

        @result
        def ice_bolt() -> str:
            """
            成功すれば氷を打つ、失敗したらraiseする
            """

            if random.randint(0, 1):
                raise Exception()
            return "ice_bolt"

        print(ice_bolt())
        print()

        # 4.MageGuildクラスをテスト
        print("Testing MageGuild...")
        result = MageGuild()

        true_name = random.choice(mage_names)
        False_name = random.choice(invalid_names)
        spell_name = random.choice(spell_names)
        magic_power = random.choice(test_powers)

        print(f"{true_name}: {result.validate_mage_name(true_name)}")
        print(f"{False_name}: {result.validate_mage_name(False_name)}")

        print(f"power({magic_power}): "
              f"{result.cast_spell(spell_name, power=magic_power)}")

    except TypeError as e:
        print(f"TypeError: {e}")


if __name__ == "__main__":
    main()
