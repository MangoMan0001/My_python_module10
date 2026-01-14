#!/usr/bin/env python3
import operator
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
    ラムダ式関数実行関数
    """

class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        ラムダ式関数実行関数
        """
    def cast_spell(self, spell_name: str, power: int) -> str:
        """
        ラムダ式関数実行関数
        """


def main() -> None:
    """
    ラムダ式関数実行関数
    """

    test_powers = [19, 18, 21, 11]
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

        # 2.power_validataorを実行
        print("Testing power_validataor...")
        result = power_validator(20)

        @result
        def big_fire_ball(power) -> str:
            """
            魔力を使って火の玉を打つ
            """

            return f"({power}) BIG FIRE BALL!!!"

        for p in test_powers:
            print(f"power({p}): {big_fire_ball(p)}")  # .なぜかpowerにうまく入らないので、引数増やしてテストしましょう

    except TypeError as e:
        print(f"TypeError: {e}")


if __name__ == "__main__":
    main()
