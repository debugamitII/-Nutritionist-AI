# -Nutritionist-AI
Nutritionist Generative AI Doctor for accessing calories and quality of food  Using Google Gemini Pro Vision
# 🥗 Food Image Calorie & Nutrition Analyzer

An AI-powered tool designed by a **pediatrician and certified nutritionist** to analyze food items from images and provide detailed insights into their **calorie content**, **nutritional composition**, and **health value**.

## 🔍 Overview

This project leverages computer vision and AI to:
- Detect and identify food items in an image
- Estimate total calorie content
- Break down the ratio of **carbohydrates**, **proteins**, **fibers**, **minerals**, **sugars**, and **fats**
- Determine whether the food is **healthy or processed**
- Provide dietary recommendations based on standard nutritional guidelines

## 📊 Output Format

Each analysis follows the below structure:

Item 1 – xxx kcal

Item 2 – xxx kcal
...
✅ Healthy Food / ⚠️ Processed Food (with warning)
Nutrient Ratio:

Carbohydrates: xx%

Proteins: xx%

Fibers: xx%

Minerals: xx%

Sugars: xx%

Fats: xx%

🥦 Recommended Daily Nutritional Intake (Adult on Diet):

Carbohydrates: 45-50%

Proteins: 25-30%

Fibers: 10-15%

Minerals: 5-7%

Sugars: <5%

Fats: 10-15%

shell
Copy
Edit

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core Programming |
| OpenCV | Image Preprocessing |
| TensorFlow/Keras or PyTorch | Food Recognition Model |
| Streamlit or Flask | Web Interface |
| Nutrition APIs | Calorie and nutrient lookup |
| Matplotlib/Plotly | Visualization of nutrient distribution |

## 📸 Sample Usage

Upload a food image and get an instant nutritional report:

![sample_output](images/sample_food_analysis.png)

Grilled Chicken – 220 kcal

Brown Rice – 180 kcal

Steamed Broccoli – 55 kcal

✅ Healthy Food ✔️

Nutrient Ratio:

Carbohydrates: 40%

Proteins: 35%

Fibers: 12%

Minerals: 5%

Sugars: 3%

Fats: 5%

markdown
Copy
Edit

## ⚠️ Warnings

- ❗ Highly processed or fried foods will trigger a health warning.
- The AI is trained on a broad dataset but accuracy may vary with rare or composite dishes.

## ✅ Ideal Use Cases

- Dieticians and nutritionists
- Health-focused individuals
- Pediatric consultations
- Calorie tracking for fitness

## 🧠 Future Improvements

- Add support for multiple cuisines
- Personalized recommendations based on age, gender, and activity level
- Integration with fitness tracking devices

## 📄 License

MIT License

## 🙌 Contributing

We welcome contributions! Please open issues or submit pull requests for improvements or bug fixes.

---

