import streamlit as st
from googletrans import Translator
from PIL import Image

translator = Translator()

# -----------------------------
# UI: Выбор языка
# -----------------------------
language = st.selectbox(
    "🌐 Выберите язык интерфейса",
    options=["de", "en", "fr", "nl", "ru", "it", "es", "pl"],
    format_func=lambda x: {
        "de": "🇩🇪 Немецкий", "en": "🇬🇧 Английский", "fr": "🇫🇷 Французский",
        "nl": "🇳🇱 Голландский", "ru": "🇷🇺 Русский", "it": "🇮🇹 Итальянский",
        "es": "🇪🇸 Испанский", "pl": "🇵🇱 Польский"
    }[x]
)

# -----------------------------
# UI: Загрузка изображения
# -----------------------------
st.title("📸 AI Меню + Акции")
st.write("Загрузите фото блюда, чтобы получить описание, перевод и акции")

image = st.file_uploader("Загрузите фото блюда", type=["jpg", "png", "jpeg"])

if image:
    st.image(image, caption="Загруженное изображение", use_column_width=True)

    # -----------------------------
    # ИМИТАЦИЯ РАСПОЗНАВАНИЯ БЛЮДА
    # -----------------------------
    detected_dish = "Pizza Margherita"
    ingredients = "Cheese, tomato, basil"
    promo = "🔥 Сегодня скидка 15%!"
    kids_bonus = "🎁 Детям сок бесплатно"

    # -----------------------------
    # Перевод
    # -----------------------------
    try:
        detected_dish_translated = translator.translate(detected_dish, dest=language).text
        ingredients_translated = translator.translate(ingredients, dest=language).text
        promo_translated = translator.translate(promo, dest=language).text
        kids_bonus_translated = translator.translate(kids_bonus, dest=language).text
    except:
        detected_dish_translated = detected_dish
        ingredients_translated = ingredients
        promo_translated = promo
        kids_bonus_translated = kids_bonus

    # -----------------------------
    # Вывод результата
    # -----------------------------
    st.markdown(f"### 🍽️ {detected_dish_translated}")
    st.markdown(f"**🧾 Состав:** {ingredients_translated}")
    st.markdown(f"**{promo_translated}**")
    st.markdown(f"**{kids_bonus_translated}**")