
import streamlit as st

st.set_page_config(
    page_title="Pizza Hub",
    page_icon="🍕",
)

st.title(":red[Welcome to pizza hub 🍕]", text_alignment="center")
st.subheader(":red[The best italian restaurant serving delicious food]")

# Same styling for every product heading
st.markdown("""
<style>
.menu-title {
    font-size: 20px;
    font-weight: 700;
    white-space: nowrap;
    margin-top: 20px;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

pizza_tab, pasta_tab, drinks_tab = st.tabs(["Pizza", "Pasta", "Drinks"])


# ==================== PIZZA TAB ====================

with pizza_tab:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=1000&q=80",
            caption="Chicken Pizza",
            width=200
        )

        st.markdown('<p class="menu-title">Chicken Pizza</p>', unsafe_allow_html=True)

        option = st.segmented_control(
            "Size:",
            options=["small", "medium", "large"],
            default="medium",
            key="pizza_size"
        )

        chicken_choose = {
            "small": 120,
            "medium": 200,
            "large": 300
        }

        st.write(f"**Price**: :red[{chicken_choose[option]}] :green[EGP]")

        quantity = st.number_input(
            "Quantity:",
            min_value=1,
            max_value=10,
            value=1,
            key="chicken_quantity"
        )

        total = chicken_choose[option] * quantity

        if st.button("Calculate Total Price", key="chicken_calculate"):
            st.write(f"**Total Price**: :red[{total}] :green[EGP]")

    with col2:
        st.image(
            "https://pizzano.co.in/assets/images/gallery/pepperoni_pizza_product_shot.png",
            caption="Pepperoni Pizza",
            width=200
        )

        st.markdown('<p class="menu-title">Pepperoni Pizza</p>', unsafe_allow_html=True)

        option = st.segmented_control(
            "Size:",
            options=["small", "medium", "large"],
            default="medium",
            key="pepperoni_size"
        )

        pepperoni_choose = {
            "small": 150,
            "medium": 250,
            "large": 350
        }

        st.write(f"**Price**: :red[{pepperoni_choose[option]}] :green[EGP]")

        quantity = st.number_input(
            "Quantity:",
            min_value=1,
            max_value=10,
            value=1,
            key="pepperoni_quantity"
        )

        total = pepperoni_choose[option] * quantity

        if st.button("Calculate Total Price", key="pepperoni_calculate"):
            st.write(f"**Total Price**: :red[{total}] :green[EGP]")

    with col3:
        st.image(
            "https://cdn.shopify.com/s/files/1/0851/3955/4638/files/Classic_Cheese_Pizza_with_Golden_Crust_and_Melted_Mozzarella.webp?v=1747591495",
            caption="Margherita Pizza",
            width=200
        )

        st.markdown('<p class="menu-title">Margherita Pizza</p>', unsafe_allow_html=True)

        option = st.segmented_control(
            "Size:",
            options=["small", "medium", "large"],
            default="medium",
            key="margherita_size"
        )

        margherita_choose = {
            "small": 100,
            "medium": 180,
            "large": 250
        }

        st.write(f"**Price**: :red[{margherita_choose[option]}] :green[EGP]")

        quantity = st.number_input(
            "Quantity:",
            min_value=1,
            max_value=10,
            value=1,
            key="margherita_quantity"
        )

        total = margherita_choose[option] * quantity

        if st.button("Calculate Total Price", key="margherita_calculate"):
            st.write(f"**Total Price**: :red[{total}] :green[EGP]")


# ==================== PASTA TAB ====================

with pasta_tab:
    pasta_col1, pasta_col2, pasta_col3 = st.columns(3)

    # Red Sauce Pasta
    with pasta_col1:
        st.image(
            "https://miro.medium.com/v2/resize:fit:736/1*HqJFqDEhRGLp73jxpkMpiA@2x.jpeg",
            caption="Red Sauce Pasta",
            width=200
        )

        st.markdown('<p class="menu-title">Red Sauce Pasta</p>', unsafe_allow_html=True)

        option = st.segmented_control(
            "Size:",
            options=["Small", "Medium", "Large"],
            default="Medium",
            key="red_sauce_size"
        )

        red_sauce_choose = {
            "Small": 80,
            "Medium": 120,
            "Large": 150
        }

        st.write(f"**Price**: :red[{red_sauce_choose[option]}] :green[EGP]")

        quantity = st.number_input(
            "Quantity:",
            min_value=1,
            max_value=10,
            value=1,
            key="red_sauce_quantity"
        )

        total = red_sauce_choose[option] * quantity

        if st.button("Calculate Total Price", key="red_sauce_calculate"):
            st.write(f"**Total Price**: :red[{total}] :green[EGP]")

    # Chicken Alfredo Pasta
    with pasta_col2:
        st.image(
            "https://myhomemaderecipe.com/assets/images/Ultimate-Comfort-Food-with-Chicken-Alfredo-hero.jpg",
            caption="Chicken Alfredo Pasta",
            width=200
        )

        st.markdown('<p class="menu-title">Chicken Alfredo Pasta</p>', unsafe_allow_html=True)

        option = st.segmented_control(
            "Size:",
            options=["Small", "Medium", "Large"],
            default="Medium",
            key="chicken_alfredo_size"
        )

        chicken_alfredo_choose = {
            "Small": 100,
            "Medium": 140,
            "Large": 180
        }

        st.write(f"**Price**: :red[{chicken_alfredo_choose[option]}] :green[EGP]")

        quantity = st.number_input(
            "Quantity:",
            min_value=1,
            max_value=10,
            value=1,
            key="chicken_alfredo_quantity"
        )

        total = chicken_alfredo_choose[option] * quantity

        if st.button("Calculate Total Price", key="chicken_alfredo_calculate"):
            st.write(f"**Total Price**: :red[{total}] :green[EGP]")

    # Pesto Pasta
    with pasta_col3:
        st.image(
            "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?auto=format&fit=crop&w=1000&q=80",
            caption="Pesto Pasta",
            width=200
        )

        st.markdown('<p class="menu-title">Pesto Pasta</p>', unsafe_allow_html=True)

        option = st.segmented_control(
            "Size:",
            options=["Small", "Medium", "Large"],
            default="Medium",
            key="pesto_size"
        )

        pesto_choose = {
            "Small": 90,
            "Medium": 130,
            "Large": 170
        }

        st.write(f"**Price**: :red[{pesto_choose[option]}] :green[EGP]")

        quantity = st.number_input(
            "Quantity:",
            min_value=1,
            max_value=10,
            value=1,
            key="pesto_quantity"
        )

        total = pesto_choose[option] * quantity

        if st.button("Calculate Total Price", key="pesto_calculate"):
            st.write(f"**Total Price**: :red[{total}] :green[EGP]")


# ==================== DRINKS TAB ====================

with drinks_tab:
    drink_col1, drink_col2, drink_col3 = st.columns(3)

    with drink_col1: 
        st.image(
            "https://static.wixstatic.com/media/cf8a7a_8b57d45e0bf34139b2f9486f56037623~mv2.jpg/v1/fill/w_2500%2Ch_2500%2Cal_c/cf8a7a_8b57d45e0bf34139b2f9486f56037623~mv2.jpg?utm_source=chatgpt.com",
             caption="Orange Juice",
             width=200
        )

        st.markdown('<p class="menu-title">Orange Juice</p>', unsafe_allow_html=True)

        st.write(f"**Price**: :red[30] :green[EGP]")
        quantity = st.number_input(
            "Quantity:",
            min_value=1,
            max_value=10,
            value=1,
            key="orange_juice_quantity"
        )
        total = 30 * quantity

        if st.button("Calculate Total Price", key="orange_juice_calculate"):
            st.write(f"**Total Price**: :red[{total}] :green[EGP]")

    with drink_col2:
        st.image(
            "https://static.wixstatic.com/media/94064a_663b580963db4712862241d304ff3833~mv2.png/v1/fill/w_480%2Ch_480%2Cal_c%2Cq_85%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/94064a_663b580963db4712862241d304ff3833~mv2.png?utm_source=chatgpt.com",
            caption="Fresh Lemonade",
            width=200
        )

        st.markdown('<p class="menu-title">Fresh Lemonade</p>', unsafe_allow_html=True)

        st.write(f"**Price**: :red[35] :green[EGP]")
        quantity = st.number_input(
            "Quantity:",
            min_value=1,
            max_value=10,
            value=1,
            key="fresh_lemonade_quantity"
        )
        total = 35 * quantity

        if st.button("Calculate Total Price", key="fresh_lemonade_calculate"):
            st.write(f"**Total Price**: :red[{total}] :green[EGP]")
    
    with drink_col3:
        st.image(
         "https://16a9564f-f8ec-42ba-a998-3027aa809e50.selstorage.ru/mosgorpitstsa-tso/1025/images/items/5f809e0c50d1d8c6a81c72bdfbaacd90.JPEG",
        width=200,
        caption="Iced Cola"
        )
        st.markdown('<p class="menu-title">Iced Cola</p>', unsafe_allow_html=True)
        st.write(f"**Price**: :red[25] :green[EGP]")
        quantity = st.number_input(
            "Quantity:",
            min_value=1,
            max_value=10,
            value=1,
            key="iced_cola_quantity"
        )
        total = 25 * quantity
        if st.button("Calculate Total Price", key="iced_cola_calculate"):
            st.write(f"**Total Price**: :red[{total}] :green[EGP]")


