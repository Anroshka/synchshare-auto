import cv2
import numpy as np
import pyautogui
import time
from pathlib import Path

class SimpleBot:
    def __init__(self, button_path: str, answer_path: str, confidence=0.8):
        self.button_path = button_path
        self.answer_path = answer_path
        self.confidence = confidence
        # Уменьшаем паузу между действиями мыши
        pyautogui.PAUSE = 0.1
        
    def find_and_click_button(self):
        try:
            # Поиск кнопки на экране
            button_location = pyautogui.locateOnScreen(
                self.button_path,
                confidence=self.confidence
            )
            
            if button_location:
                # Получаем центр кнопки и кликаем по нему
                button_center = pyautogui.center(button_location)
                pyautogui.click(button_center)
                print(f"Успешно кликнули по кнопке: {button_center}")
                
                # Сохраняем начальную позицию для последующих движений
                start_x, start_y = button_center
                
                # Первое движение: 78 вправо, 24 вниз
                pyautogui.moveTo(start_x + 78, start_y + 24)
                pyautogui.click()
                time.sleep(0.1)
                
                # Второе движение: 195 вправо, 26 вниз от начальной позиции
                pyautogui.moveTo(start_x + 195, start_y + 26)
                pyautogui.click()
                time.sleep(0.1)
                
                return True
            else:
                print("Кнопка не найдена")
                return False
                
        except Exception as e:
            print(f"Произошла ошибка при поиске кнопки: {e}")
            return False
    
    def find_and_click_answer(self):
        try:
            # Поиск кнопки ответа на экране
            answer_location = pyautogui.locateOnScreen(
                self.answer_path,
                confidence=self.confidence
            )
            
            if answer_location:
                # Получаем центр кнопки ответа и кликаем по нему
                answer_center = pyautogui.center(answer_location)
                pyautogui.click(answer_center)
                print("Успешно кликнули по кнопке ответа")
                return True
            else:
                print("Кнопка ответа не найдена")
                return False
        except Exception as e:
            print(f"Ошибка при поиске кнопки ответа: {e}")
            return False

    def run(self):
        print("Бот запущен. Для остановки нажмите Ctrl+C")
        try:
            while True:
                if self.find_and_click_button():
                    time.sleep(0.2)  # Уменьшаем паузу после кликов
                    self.find_and_click_answer()
                time.sleep(0.5)  # Уменьшаем паузу между циклами
                
        except KeyboardInterrupt:
            print("\nБот остановлен пользователем")

if __name__ == "__main__":
    # Пути к изображениям
    button_path = "button.png"
    answer_path = "answer.png"
    
    # Создаем и запускаем бота
    bot = SimpleBot(button_path, answer_path, confidence=0.8)
    bot.run()
