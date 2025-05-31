from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO
import datetime

from owm_api import get_direction


class WeatherWidgetGenerator:
    DEFAULT_ICON = '02d'  # Иконка по умолчанию

    fonts = {
        'main': ImageFont.truetype("arial.ttf", 24),
        'secondary': ImageFont.truetype("arial.ttf", 14)
    }

    def generate_widget(self, weather_data: dict) -> BytesIO:
        """Генерация виджета с защитой от ошибок"""
        try:
            # Проверка обязательных данных
            if not weather_data or 'temp' not in weather_data:
                raise ValueError("Invalid weather data")

            # Создаем основу
            img = Image.new('RGB', (320, 160), '#202124')
            draw = ImageDraw.Draw(img)

            # Загружаем иконку (с fallback)
            icon_code = weather_data.get('icon', self.DEFAULT_ICON)
            try:
                icon = Image.open(f"icons/{icon_code}@2x.png").resize((60, 60))
            except:
                icon = Image.open(f"icons/{self.DEFAULT_ICON}.png").resize((60, 60))

            img.paste(icon, (10, 10), icon)

            # Добавляем текст
            draw.text((80, 15), f"{weather_data['temp']}°C", font=self.fonts['main'], fill="#4285F4")
            draw.text((80, 45), f"Ощущается: {weather_data.get('feels_like', 'N/A')}°C", font=self.fonts['secondary'],
                      fill="white")

            return self._prepare_output(img)

        except Exception as e:
            print(f"Widget generation failed: {e}")
            return self._generate_error_widget()

    def _prepare_output(self, img: Image) -> BytesIO:
        """Конвертация в BytesIO"""
        buf = BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        return buf

    def _generate_error_widget(self) -> BytesIO:
        """Виджет с сообщением об ошибке"""
        img = Image.new('RGB', (320, 160), '#202124')
        draw = ImageDraw.Draw(img)
        draw.text((50, 50), "Ошибка генерации", fill="red")
        return self._prepare_output(img)