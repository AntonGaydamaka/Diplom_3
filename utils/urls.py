# Базовый URL приложения
BASE_URL = 'https://qa-stellarburgers.education-services.ru'

# Основные URL пользовательского интерфейса
# ========================================
# Главная страница приложения
MAIN_URL = f'{BASE_URL}/'

# Страница личного кабинета
ACCOUNT_URL = f'{BASE_URL}/account'

# История заказов в личном кабинете
ACCOUNT_ORDER_HISTORY_URL = f'{BASE_URL}/account/order-history'

# Лента заказов
FEED_URL = f'{BASE_URL}/feed'

# Страница входа в систему
LOGIN_URL = f'{BASE_URL}/login'

# Страница восстановления пароля
FORGOT_PASSWORD_URL = f'{BASE_URL}/forgot-password'

# Страница сброса пароля
RESET_PASSWORD_URL = f'{BASE_URL}/reset-password'

# URL API эндпоинтов
# =================
# Эндпоинт для регистрации нового пользователя
CREATE_USER = f'{BASE_URL}/api/auth/register'

# Эндпоинт для удаления пользователя
DELETE_USER = f'{BASE_URL}/api/auth/user'
