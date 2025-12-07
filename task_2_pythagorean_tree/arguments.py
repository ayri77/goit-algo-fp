"""
Модуль для обробки аргументів командного рядка та інтерактивного вводу.

Відповідає за парсинг аргументів та збір параметрів від користувача.
"""

import argparse
import sys
from typing import Literal


class ArgumentParser:
    """Клас для парсингу аргументів командного рядка."""
    
    def __init__(self) -> None:
        self.parser = self._create_parser()
    
    def _create_parser(self) -> argparse.ArgumentParser:
        """Створює та налаштовує argparse парсер."""
        parser = argparse.ArgumentParser(
            description="Візуалізація фрактала 'дерево Піфагора'",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Приклади використання:
  python main.py                                    # Інтерактивний режим (matplotlib)
  python main.py --level 3                          # Рівень 3 через аргумент
  python main.py -l 5 -v turtle                     # Turtle візуалізація
  python main.py -l 3 -v turtle -m tree             # Turtle з трикутниками
  python main.py -l 3 --size 150 --angle 45          # З додатковими параметрами
  python main.py -l 4 -v turtle -m squares --turtle-speed 3  # Швидка turtle візуалізація
            """
        )
        
        parser.add_argument(
            "--level", "-l",
            type=int,
            default=None,
            help="Рівень рекурсії (0-10, за замовчуванням - інтерактивний режим)"
        )
        parser.add_argument(
            "--size", "-s",
            type=float,
            default=100.0,
            help="Розмір початкового квадрата (за замовчуванням: 100)"
        )
        parser.add_argument(
            "--angle", "-a",
            type=float,
            default=45.0,
            help="Кут розгалуження в градусах (за замовчуванням: 45)"
        )
        parser.add_argument(
            "--start-x",
            type=float,
            default=0.0,
            help="X координата початку (за замовчуванням: 0)"
        )
        parser.add_argument(
            "--start-y",
            type=float,
            default=0.0,
            help="Y координата початку (за замовчуванням: 0)"
        )
        parser.add_argument(
            "--visualization", "-v",
            type=str,
            choices=['matplotlib', 'turtle'],
            default='matplotlib',
            help="Тип візуалізації: 'matplotlib' або 'turtle' (за замовчуванням: matplotlib)"
        )
        parser.add_argument(
            "--mode", "-m",
            type=str,
            choices=['squares', 'tree'],
            default='tree',
            help="Режим побудови: 'tree' (тільки лінії скелета) або 'squares' (квадрати + трикутники)"
        )
        parser.add_argument(
            "--turtle-speed",
            type=int,
            default=5,
            help="Швидкість малювання turtle (0-50, де 0 - найшвидше, за замовчуванням: 5)"
        )
        
        return parser
    
    def parse(self) -> argparse.Namespace:
        """Парсить аргументи командного рядка."""
        return self.parser.parse_args()


class InteractiveInputHandler:
    """Клас для обробки інтерактивного вводу від користувача."""
    
    @staticmethod
    def get_level() -> int:
        """Запитує у користувача рівень рекурсії."""
        while True:
            try:
                level = int(input("Введіть рівень рекурсії (0-10, рекомендовано 3-5): "))
                if 0 <= level <= 10:
                    return level
                else:
                    print("Будь ласка, введіть число від 0 до 10.")
            except ValueError:
                print("Будь ласка, введіть ціле число.")
            except KeyboardInterrupt:
                print("\nОперацію скасовано.")
                sys.exit(0)
    
    @staticmethod
    def get_visualization() -> Literal['matplotlib', 'turtle']:
        """Запитує у користувача тип візуалізації з меню вибору."""
        while True:
            try:
                print("\nВиберіть тип візуалізації:")
                print("  1) matplotlib (рекомендовано)")
                print("  2) turtle")
                choice = input("Ваш вибір [1]: ").strip()
                
                if not choice or choice == '1':
                    return 'matplotlib'
                elif choice == '2':
                    return 'turtle'
                else:
                    print("Будь ласка, введіть 1 або 2.")
            except KeyboardInterrupt:
                print("\nОперацію скасовано.")
                sys.exit(0)
    
    @staticmethod
    def get_mode(visualization: str = 'matplotlib') -> Literal['tree', 'squares']:
        """Запитує у користувача режим побудови з меню вибору."""
        while True:
            try:
                default_mode = 'tree' if visualization == 'matplotlib' else 'squares'
                default_num = '1' if default_mode == 'tree' else '2'
                
                print("\nВиберіть режим побудови:")
                print("  1) tree (лінії скелета дерева)")
                print("  2) squares (квадрати + трикутники)")
                choice = input(f"Ваш вибір [{default_num}]: ").strip()
                
                if not choice:
                    return default_mode
                if choice == '1':
                    return 'tree'
                elif choice == '2':
                    return 'squares'
                else:
                    print("Будь ласка, введіть 1 або 2.")
            except KeyboardInterrupt:
                print("\nОперацію скасовано.")
                sys.exit(0)
    
    @staticmethod
    def get_size() -> float:
        """Запитує у користувача розмір початкового квадрата."""
        while True:
            try:
                size_str = input("Введіть розмір початкового квадрата [100]: ").strip()
                if not size_str:
                    return 100.0
                size = float(size_str)
                if size > 0:
                    return size
                else:
                    print("Розмір повинен бути більше 0.")
            except ValueError:
                print("Будь ласка, введіть дійсне число.")
            except KeyboardInterrupt:
                print("\nОперацію скасовано.")
                sys.exit(0)
    
    @staticmethod
    def get_angle() -> float:
        """Запитує у користувача кут розгалуження."""
        while True:
            try:
                angle_str = input("Введіть кут розгалуження в градусах [45]: ").strip()
                if not angle_str:
                    return 45.0
                angle = float(angle_str)
                if 0 < angle < 180:
                    return angle
                else:
                    print("Кут повинен бути від 0 до 180 градусів.")
            except ValueError:
                print("Будь ласка, введіть дійсне число.")
            except KeyboardInterrupt:
                print("\nОперацію скасовано.")
                sys.exit(0)
    
    @staticmethod
    def get_turtle_speed() -> int:
        """Запитує у користувача швидкість turtle."""
        while True:
            try:
                speed_str = input("Введіть швидкість turtle (0-50, де 0 - найшвидше) [5]: ").strip()
                if not speed_str:
                    return 5
                speed = int(speed_str)
                if 0 <= speed <= 50:
                    return speed
                else:
                    print("Швидкість повинна бути від 0 до 50.")
            except ValueError:
                print("Будь ласка, введіть ціле число.")
            except KeyboardInterrupt:
                print("\nОперацію скасовано.")
                sys.exit(0)
    
    @staticmethod
    def get_start_position() -> tuple[float, float]:
        """Запитує у користувача початкову позицію."""
        while True:
            try:
                x_str = input("Введіть X координату початку [0]: ").strip()
                y_str = input("Введіть Y координату початку [0]: ").strip()
                
                x = float(x_str) if x_str else 0.0
                y = float(y_str) if y_str else 0.0
                
                return (x, y)
            except ValueError:
                print("Будь ласка, введіть дійсні числа.")
            except KeyboardInterrupt:
                print("\nОперацію скасовано.")
                sys.exit(0)
    
    @classmethod
    def collect_all_parameters(cls) -> dict[str, int | float | str]:
        """
        Збирає всі параметри від користувача в інтерактивному режимі.
        
        Returns:
            dict: Словник з усіма параметрами
        """
        print("=" * 60)
        print("Інтерактивний режим налаштування")
        print("=" * 60)
        print("(Натисніть Enter для використання значення за замовчуванням)\n")
        
        level = cls.get_level()
        visualization = cls.get_visualization()
        mode = cls.get_mode(visualization)
        size = cls.get_size()
        angle = cls.get_angle()
        
        if visualization == 'turtle':
            turtle_speed = cls.get_turtle_speed()
        else:
            turtle_speed = 5  # За замовчуванням
        
        start_x, start_y = cls.get_start_position()
        
        return {
            'level': level,
            'visualization': visualization,
            'mode': mode,
            'size': size,
            'angle': angle,
            'turtle_speed': turtle_speed,
            'start_x': start_x,
            'start_y': start_y
        }


class ParametersValidator:
    """Клас для валідації параметрів."""
    
    @staticmethod
    def validate_level(level: int) -> int:
        """Валідує рівень рекурсії."""
        if not (0 <= level <= 10):
            raise ValueError("Рівень рекурсії повинен бути від 0 до 10.")
        return level
    
    @staticmethod
    def validate_turtle_speed(speed: int) -> int:
        """Валідує швидкість turtle."""
        if not (0 <= speed <= 50):
            return 5  # Повертаємо значення за замовчуванням
        return speed
    
    @staticmethod
    def validate_mode_and_visualization(
        mode: str,
        visualization: str
    ) -> tuple[str, str]:
        """
        Валідує комбінацію режиму та візуалізації.
        
        Обидва режими доступні для обох типів візуалізації.
        """
        return mode, visualization


class ParametersProcessor:
    """Клас для обробки та об'єднання параметрів з аргументів та інтерактивного вводу."""
    
    def __init__(self) -> None:
        self.arg_parser = ArgumentParser()
        self.input_handler = InteractiveInputHandler()
        self.validator = ParametersValidator()
    
    def process(self) -> dict[str, int | float | str]:
        """
        Обробляє аргументи та повертає фінальні параметри.
        
        Returns:
            dict: Словник з усіма параметрами для побудови дерева
        """
        args = self.arg_parser.parse()
        
        # Визначаємо, чи потрібен інтерактивний режим
        interactive_mode = args.level is None
        
        if interactive_mode:
            # Збираємо параметри інтерактивно
            params = self.input_handler.collect_all_parameters()
        else:
            # Використовуємо параметри з аргументів
            params = {
                'level': args.level,
                'visualization': args.visualization,
                'mode': args.mode,
                'size': args.size,
                'angle': args.angle,
                'turtle_speed': args.turtle_speed,
                'start_x': args.start_x,
                'start_y': args.start_y
            }
        
        # Валідація параметрів
        try:
            params['level'] = self.validator.validate_level(params['level'])
        except ValueError as e:
            print(f"Помилка: {e}")
            sys.exit(1)
        
        params['turtle_speed'] = self.validator.validate_turtle_speed(params['turtle_speed'])
        params['mode'], params['visualization'] = self.validator.validate_mode_and_visualization(
            params['mode'], 
            params['visualization']
        )
        
        return params

