import streamlit as st
import cohere

# Initialize Cohere client
co = cohere.Client('cCaBb430kMioiub17v2gOo34tK21SvPi7sFYIQML')  # ⚠️ Replace with your actual API key

# Streamlit app setup
st.set_page_config(page_title="Recipe Generator", page_icon="🍲")
st.title("🍽️ AI Recipe Generator with Cohere")

# Input from user
ingredients = st.text_input("Enter the ingredients you have:", placeholder="e.g. chicken, tomatoes, garlic")

# Function to get recipe from Cohere
def get_recipe(ingredients):
    response = co.generate(
        model='command-r-plus',
        prompt=f'Give me a recipe using {ingredients}.',
        max_tokens=500
    )
    return response.generations[0].text.strip()

# Button to trigger generation
if st.button("Generate Recipe"):
    if ingredients:
        with st.spinner("Cooking up your recipe..."):
            try:
                recipe = get_recipe(ingredients)
                st.subheader("🍛 Recipe Suggestion")
                st.markdown(recipe)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter some ingredients first.")
