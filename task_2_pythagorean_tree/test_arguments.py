"""
Юніт-тести для модуля обробки аргументів та параметрів.

Перевіряє коректність парсингу аргументів, інтерактивного вводу та валідації.
"""

import pytest
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Додаємо директорію завдання до шляху
sys.path.insert(0, str(Path(__file__).parent))

from arguments import (
    ArgumentParser,
    InteractiveInputHandler,
    ParametersValidator,
    ParametersProcessor
)


@pytest.mark.unit
class TestInteractiveInputHandler:
    """Тести для інтерактивного вводу параметрів."""
    
    @patch('builtins.input', return_value='3')
    def test_get_level_valid(self, mock_input):
        """Тест отримання рівня від користувача з валідним значенням."""
        result = InteractiveInputHandler.get_level()
        assert result == 3
        assert mock_input.called
    
    @patch('builtins.input', side_effect=['15', '5'])
    def test_get_level_invalid_then_valid(self, mock_input):
        """Тест отримання рівня з невалідним, потім валідним значенням."""
        result = InteractiveInputHandler.get_level()
        assert result == 5
        assert mock_input.call_count == 2
    
    @patch('builtins.input', return_value='1')
    def test_get_visualization_matplotlib(self, mock_input):
        """Тест отримання типу візуалізації matplotlib."""
        result = InteractiveInputHandler.get_visualization()
        assert result == 'matplotlib'
    
    @patch('builtins.input', return_value='2')
    def test_get_visualization_turtle(self, mock_input):
        """Тест отримання типу візуалізації turtle."""
        result = InteractiveInputHandler.get_visualization()
        assert result == 'turtle'
    
    @patch('builtins.input', return_value='')
    def test_get_visualization_default(self, mock_input):
        """Тест отримання типу візуалізації за замовчуванням."""
        result = InteractiveInputHandler.get_visualization()
        assert result == 'matplotlib'
    
    @patch('builtins.input', return_value='1')
    def test_get_mode_tree(self, mock_input):
        """Тест отримання режиму tree."""
        result = InteractiveInputHandler.get_mode('matplotlib')
        assert result == 'tree'
    
    @patch('builtins.input', return_value='2')
    def test_get_mode_squares(self, mock_input):
        """Тест отримання режиму squares."""
        result = InteractiveInputHandler.get_mode('matplotlib')
        assert result == 'squares'
    
    @patch('builtins.input', return_value='')
    def test_get_mode_default_matplotlib(self, mock_input):
        """Тест отримання режиму за замовчуванням для matplotlib."""
        result = InteractiveInputHandler.get_mode('matplotlib')
        assert result == 'tree'  # За замовчуванням для matplotlib
    
    @patch('builtins.input', return_value='')
    def test_get_mode_default_turtle(self, mock_input):
        """Тест отримання режиму за замовчуванням для turtle."""
        result = InteractiveInputHandler.get_mode('turtle')
        assert result == 'squares'  # За замовчуванням для turtle


@pytest.mark.unit
class TestParametersValidator:
    """Тести для валідації параметрів."""
    
    def test_validate_level_valid(self):
        """Тест валідації валідного рівня."""
        assert ParametersValidator.validate_level(0) == 0
        assert ParametersValidator.validate_level(5) == 5
        assert ParametersValidator.validate_level(10) == 10
    
    def test_validate_level_invalid(self):
        """Тест валідації невалідного рівня."""
        with pytest.raises(ValueError):
            ParametersValidator.validate_level(-1)
        with pytest.raises(ValueError):
            ParametersValidator.validate_level(11)
        with pytest.raises(ValueError):
            ParametersValidator.validate_level(100)
    
    def test_validate_turtle_speed_valid(self):
        """Тест валідації валідної швидкості turtle."""
        assert ParametersValidator.validate_turtle_speed(0) == 0
        assert ParametersValidator.validate_turtle_speed(5) == 5
        assert ParametersValidator.validate_turtle_speed(50) == 50
    
    def test_validate_turtle_speed_invalid(self):
        """Тест валідації невалідної швидкості turtle (повертає значення за замовчуванням)."""
        assert ParametersValidator.validate_turtle_speed(-1) == 5
        assert ParametersValidator.validate_turtle_speed(51) == 5
    
    def test_validate_mode_and_visualization(self):
        """Тест валідації комбінації режиму та візуалізації."""
        mode, viz = ParametersValidator.validate_mode_and_visualization('tree', 'matplotlib')
        assert mode == 'tree'
        assert viz == 'matplotlib'
        
        mode, viz = ParametersValidator.validate_mode_and_visualization('squares', 'turtle')
        assert mode == 'squares'
        assert viz == 'turtle'


@pytest.mark.unit
class TestParametersProcessor:
    """Тести для обробки параметрів."""
    
    @patch('arguments.ArgumentParser.parse')
    def test_process_with_command_line_args(self, mock_parse):
        """Тест обробки параметрів з командного рядка."""
        # Створюємо mock об'єкт для args
        mock_args = MagicMock()
        mock_args.level = 2
        mock_args.size = 150.0
        mock_args.angle = 30.0
        mock_args.visualization = 'matplotlib'
        mock_args.mode = 'tree'
        mock_args.turtle_speed = 5
        mock_args.start_x = 0.0
        mock_args.start_y = 0.0
        mock_parse.return_value = mock_args
        
        processor = ParametersProcessor()
        params = processor.process()
        
        assert params['level'] == 2
        assert params['size'] == 150.0
        assert params['angle'] == 30.0
    
    @patch('arguments.ArgumentParser.parse')
    @patch('arguments.InteractiveInputHandler.collect_all_parameters')
    def test_process_interactive_mode(self, mock_collect, mock_parse):
        """Тест обробки параметрів в інтерактивному режимі."""
        # Створюємо mock об'єкт для args з level=None (інтерактивний режим)
        mock_args = MagicMock()
        mock_args.level = None
        mock_parse.return_value = mock_args
        
        mock_collect.return_value = {
            'level': 3,
            'size': 100,
            'angle': 45,
            'start_x': 0,
            'start_y': 0,
            'visualization': 'matplotlib',
            'mode': 'tree',
            'turtle_speed': 5
        }
        
        processor = ParametersProcessor()
        params = processor.process()
        
        assert params['level'] == 3
        assert mock_collect.called
    
    @patch('arguments.ArgumentParser.parse')
    def test_process_default_values(self, mock_parse):
        """Тест обробки параметрів зі значеннями за замовчуванням."""
        # Створюємо mock об'єкт для args
        mock_args = MagicMock()
        mock_args.level = 2
        mock_args.size = 100.0  # За замовчуванням
        mock_args.angle = 45.0  # За замовчуванням
        mock_args.visualization = 'matplotlib'  # За замовчуванням
        mock_args.mode = 'tree'  # За замовчуванням
        mock_args.turtle_speed = 5  # За замовчуванням
        mock_args.start_x = 0.0
        mock_args.start_y = 0.0
        mock_parse.return_value = mock_args
        
        processor = ParametersProcessor()
        params = processor.process()
        
        # Перевіряємо, що є значення за замовчуванням
        assert 'size' in params
        assert 'angle' in params
        assert 'visualization' in params
        assert 'mode' in params
    
    @patch('arguments.ArgumentParser.parse')
    def test_process_validation_error(self, mock_parse):
        """Тест обробки помилки валідації."""
        # Створюємо mock об'єкт для args з невалідним рівнем
        mock_args = MagicMock()
        mock_args.level = 15  # Невалідний рівень
        mock_args.size = 100.0
        mock_args.angle = 45.0
        mock_args.visualization = 'matplotlib'
        mock_args.mode = 'tree'
        mock_args.turtle_speed = 5
        mock_args.start_x = 0.0
        mock_args.start_y = 0.0
        mock_parse.return_value = mock_args
        
        processor = ParametersProcessor()
        
        with patch('sys.exit') as mock_exit:
            processor.process()
            # Перевіряємо, що sys.exit був викликаний через помилку валідації
            assert mock_exit.called

